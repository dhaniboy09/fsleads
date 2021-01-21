import uuid

from django.db import models


class Lead(models.Model):
    created_timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    last_updated_timestamp = models.DateTimeField(auto_now=True, db_index=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    has_been_contacted = models.BooleanField(default=False)

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=80)

    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "id={id}; first_name={first_name} last_name={last_name}".format(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
        )

    def __repr__(self):
        return "{name}: {unicode_str}".format(
            name=self.__class__.__name__,
            unicode_str=self.__unicode__(),
        )
