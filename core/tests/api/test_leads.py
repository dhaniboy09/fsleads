from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from faker import Faker

from core.authorization import LeadApiKeyPermission
from core.models import Lead

fake = Faker()


def generate_random_lead():
    return {
        "first_name": fake.name(),
        "last_name": fake.name(),
        "email": fake.email()
    }


class LeadsAPITest(APITestCase):
    REQUIRED_HEADERS = {'HTTP_{}'.format(LeadApiKeyPermission.X_API_KEY_HEADER): settings.LEADS_API_KEY}

    def test_authorization(self):
        response = self.client.get(reverse('leads-api-list'))
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_invalid_payload(self):
        invalid_payload = {
            "first_name": "",
            "last_name": "",
            "email": "cvb@"
        }

        initial_lead_count = Lead.objects.all().count()
        response = self.client.post(reverse('leads-api-list'), data=invalid_payload, format='json',
                                    **self.REQUIRED_HEADERS)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

        current_lead_count = Lead.objects.all().count()
        self.assertEqual(initial_lead_count, current_lead_count)

    def test_create_lead(self):
        payload = generate_random_lead()
        response = self.client.post(reverse('leads-api-list'), data=payload, format='json', **self.REQUIRED_HEADERS)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        lead_id = response.data.get('id')
        lead_obj = Lead.objects.get(id=lead_id)
        self.assertEqual(response.data.get('id'), lead_id)
        self.assertEqual(response.data.get('first_name'), payload['first_name'])
        self.assertEqual(response.data.get('last_name'), payload['last_name'])
        self.assertEqual(response.data.get('email'), payload['email'])
        self.assertEqual(response.data.get('notes'), None)
        self.assertEqual(response.data.get('created_timestamp'), lead_obj.created_timestamp.strftime('%m/%d/%Y'))
        self.assertEqual(response.data.get('last_updated_timestamp'),
                         lead_obj.last_updated_timestamp.strftime('%m/%d/%Y'))

    def test_update_lead(self):
        initial_payload = generate_random_lead()
        lead_obj = Lead.objects.create(**initial_payload)

        update_payload = generate_random_lead()
        response = self.client.put(reverse('leads-api-detail', kwargs={'pk': lead_obj.id}), data=update_payload,
                                   format='json', **self.REQUIRED_HEADERS)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        lead_obj = Lead.objects.get(id=lead_obj.id)
        self.assertEqual(lead_obj.first_name, update_payload['first_name'])
        self.assertEqual(lead_obj.last_name, update_payload['last_name'])
        self.assertEqual(lead_obj.email, update_payload['email'])

    def test_delete_lead(self):
        payload = generate_random_lead()
        lead_obj = Lead.objects.create(**payload)

        lead_obj_id = lead_obj.id
        response = self.client.delete(reverse('leads-api-detail', kwargs={'pk': lead_obj_id}), **self.REQUIRED_HEADERS)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        with self.assertRaises(Lead.DoesNotExist):
            Lead.objects.get(id=lead_obj_id)
