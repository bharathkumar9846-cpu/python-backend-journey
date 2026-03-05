students = [
    {"name": "Bharath", "marks": 90},
    {"name": "Rahul", "marks": 85},
    {"name": "Anitha", "marks": 92}
]
largest = 0
top_name = str()
for i in students:
    if i.get("marks") > largest:
        largest = i["marks"]
        top_name = i.get("name")
print(top_name)