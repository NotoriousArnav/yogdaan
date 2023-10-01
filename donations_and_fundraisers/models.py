from django.db import models
import uuid
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    head_person = models.ForeignKey(
                User,
                on_delete=models.CASCADE
            )
    id = models.UUIDField(
                default=uuid.uuid4,
                primary_key=True,
                null=False
            )
    name = models.CharField(
                max_length=600,
                default=""
            )
    bio = RichTextField()
   
    def __str__(self):
        return f"{self.name} - {self.head_person.first_name} {self.head_person.last_name}"

    def __repr__(self):
        return self.__str__()

class FundraiserCampaign(models.Model):
    organization = models.ForeignKey(
                Organization,
                on_delete=models.CASCADE,
                default=""
            )
    id = models.UUIDField(
                default=uuid.uuid4,
                primary_key=True,
                null=False
            )
    publish_date = models.DateTimeField(auto_now_add=True)
    description = RichTextField()
    name = models.CharField(
                max_length=500
            )

    def campaignType(self):
        return 'Fundraiser'

    def __str__(self):
        return f"\"{self.name}\" Organised by {self.organization.name}"

    def __repr__(self):
        return self.__str__()

class DonationCampaign(models.Model):
    id =  models.UUIDField(
                default=uuid.uuid4,
                primary_key=True,
                null=False
            )
    name = models.CharField(max_length=500)
    description = RichTextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    organiser = models.ForeignKey(
                User,
                on_delete = models.CASCADE
            )
    organization = models.ForeignKey(
                Organization,
                on_delete=models.CASCADE,
                default=""
            )

    def __str__(self):
        return f"\"{self.name}\" Organised by {self.organization.name}"

    def __repr__(self):
        return self.__str__()

    def campaignType(self):
        return 'Donation'



