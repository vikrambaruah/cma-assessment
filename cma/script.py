from cma.main.models import OfficerData
import csv
with open('officer_data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader) 

    for row in csv_reader:
        OfficerData.objects.create(
            company_number=row[0],
            person_number=row[1],
            appointment_date=row[2],
            postcode=row[3],
            date_of_birth=row[4],
            title=row[5],
            first_name=row[6],
            last_name=row[7],
            honours=row[8],
            care_of=row[9],
            po_box=row[10],
            address1=row[11],
            address2=row[12],
            town=row[13],
            county=row[14],
            country=row[15]
        )