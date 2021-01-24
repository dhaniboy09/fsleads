from django.core.exceptions import ValidationError
from django.core.validators import validate_email as check_valid_email
from rest_framework import mixins, viewsets, serializers
from rest_framework.fields import SerializerMethodField

from core.authorization import LeadApiKeyPermission
from core.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    created_timestamp = SerializerMethodField()
    last_updated_timestamp = SerializerMethodField()

    class Meta:
        model = Lead
        fields = ('id', 'first_name', 'last_name', 'email', 'has_been_contacted', 'notes', 'created_timestamp',
                  'last_updated_timestamp')

    def get_created_timestamp(self, obj):
        return obj.created_timestamp.strftime('%m/%d/%Y')

    def get_last_updated_timestamp(self, obj):
        return obj.last_updated_timestamp.strftime('%m/%d/%Y')

    def validate_email(self, value):
        try:
            check_valid_email(value)
        except ValidationError:
            raise serializers.ValidationError('Email is Invalid')
        else:
            return value


class LeadsViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Lead.objects.all().order_by('-last_updated_timestamp')
    serializer_class = LeadSerializer
    permission_classes = (LeadApiKeyPermission,)
