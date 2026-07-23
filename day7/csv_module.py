# CSV files are one of the most common formats used for storing tabular data. You'll frequently work with them in data processing, automation, and backend development.
#CSV stands for Comma-Separated Values.

import csv

with open("day7/students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


print("\n")


with open("day7/students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)      # Skip header

    for row in reader:
        print(row)


print("\n")


#writing to a csv
with open("day7/students1.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Ayaan", 22, "Delhi"])
    writer.writerow(["Rahul", 24, "Mumbai"])

print("\n")


#will read csv as a dictionary
# with open("students.csv") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row)



# writing csv as dictioanry
# with open("students.csv", "w", newline="") as file:
#     fields = ["Name", "Age", "City"]

#     writer = csv.DictWriter(file, fieldnames=fields)

#     writer.writeheader()

#     writer.writerow({
#         "Name": "Ayaan",
#         "Age": 22,
#         "City": "Delhi"
#     })


# change of delimiter
# with open("students.csv") as file:
#     reader = csv.reader(file, delimiter=";")

#     for row in reader:
#         print(row)