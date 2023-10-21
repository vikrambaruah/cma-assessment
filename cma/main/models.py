from django.db import models

# Create your models here.
class OfficerData(models.Model):
    company_number = models.CharField(max_length=20)
    person_number = models.CharField(max_length=20)
    appointment_date = models.CharField(max_length=8, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    date_of_birth = models.CharField(max_length=6, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    honours = models.CharField(max_length=255, null=True, blank=True)
    care_of = models.CharField(max_length=255, null=True, blank=True)
    po_box = models.CharField(max_length=255, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    town = models.CharField(max_length=255, null=True, blank=True)
    county = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)