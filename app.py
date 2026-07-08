import json

with open("students.json", "r") as f:
    students = json.load(f)

topper = max(students, key=lambda x: x["marks"])

print("Topper:", topper["name"])
print("Marks:", topper["marks"])
