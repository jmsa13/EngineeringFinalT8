import csv

columns = ['Company Name', 'Incident Date', 'Amount of Users Affected']


with open("../CompanyData.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, columns, delimiter=",")
    writer.writeheader()

    writer.writerow({"Company Name": "Uber Breach", "Incident Date": 2014, "Amount of Users Affected": 57e6})
    writer.writerow({"Company Name": "Imperva", "Incident Date": 2018, "Amount of Users Affected": 30e6})
    writer.writerow({"Company Name": "Chegg", "Incident Date": 2018, "Amount of Users Affected": 40e6})
    writer.writerow({"Company Name": "Cisco WebEx", "Incident Date": 2020, "Amount of Users Affected": 45e6})
    writer.writerow({"Company Name": "Microsoft", "Incident Date": 2023,
                     "Amount of Users Affected": 100e6})




