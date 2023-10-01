from django.shortcuts import render
from .models import *

# Create your views here.
def dnf(request):
    d = DonationCampaign.objects.all() 
    f = FundraiserCampaign.objects.all() 
    context = {
            'dt': {
                    'donations_campaigns': d,
                    'fundraiser_campaigns': f
            }
        }
    return render(request, 'dnf.html', context=context)
