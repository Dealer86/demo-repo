# people = {
#     "Carter": "0748 000 000",
#     "David": "0748 001 001"
# }

# name = input("Name: ")

# if name in people:
#     number = people[name]
#     print("Number: ",number)

# import csv

# with open("phonebook.csv","a") as file:
#     name = input("Name: ")
#     number = input("Number: ")
#     writer = csv.writer(file)
#     writer.writerow([name,number])
import re
password = input("Password: ").lower().strip()

if re.search(r"^\w+@\w+\.com|net|org|edu$",password):
    print("Valid")
else:
    print("Invalid")
