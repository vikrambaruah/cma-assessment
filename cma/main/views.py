from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from .models import OfficerData
import json
import csv
# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,'main/index.html')
    def post (self,request):
        return render(request,'main/index.html')
class Dashboard(View):
    def get(self, request):
        country = request.GET.get('country','')
        company_number = request.GET.get('company_number','')
        

    # Start with all records
        officer_data = OfficerData.objects.all()

    # Apply filters if provided
        if company_number:
            officer_data = officer_data.filter(company_number=company_number)

        if country:
            officer_data = officer_data.filter(country__icontains=country)


        return render(request, 'main/dashboard.html', {
        'officer_data': officer_data,
        'selected_company_number': company_number,
        'selected_country': country,
        })
# class DownloadCSVTime(View):
#     def get(self, request):
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="data.csv"'
        
        

#         # Fetch data from the database
#         data = OfficerData.objects.all()

#         # Create a CSV writer
#         writer = csv.writer(response)
#         writer.writerow(["Company Number", "Person Number", "Appointment Date", "Postcode", "Date of Birth", "Title", "First Name", "Last Name", "Honours", "Care Of", "PO Box", "Address 1", "Address 2", "Town", "County", "Country"])

#         # Write data rows to the CSV
#         for item in data:
#             writer.writerow([
#                 item.component,
#                 item.component_name,
#                 item.component_id,
#                 item.timestamp,
#                 item.sequence,
#                 item.value,
#             ])

#         return response

