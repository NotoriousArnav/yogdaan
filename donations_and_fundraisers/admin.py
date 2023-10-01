from django.contrib import admin
from .models import DonationCampaign, Organization, FundraiserCampaign

# Register your models here.
admin.site.register(DonationCampaign)
admin.site.register(FundraiserCampaign)
admin.site.register(Organization)
