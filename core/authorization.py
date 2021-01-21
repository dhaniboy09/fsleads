from django.conf import settings
from rest_framework.permissions import BasePermission


class LeadApiKeyPermission(BasePermission):
    # This is the expected header when making an actual request
    X_API_KEY_HEADER = 'X-API-Key'  # type: str

    def has_permission(self, request, view=None):
        api_key = request.headers.get(self.X_API_KEY_HEADER)
        if not api_key or api_key != settings.LEADS_API_KEY:
            return False
        return True
