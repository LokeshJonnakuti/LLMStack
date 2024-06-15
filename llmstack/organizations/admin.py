from django.contrib import admin

from .models import Organization
from .models import OrganizationSettings


admin.site.register(Organization)
admin.site.register(OrganizationSettings)
