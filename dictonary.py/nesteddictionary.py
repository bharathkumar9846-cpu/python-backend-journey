students = {
    "101": {"name": "Bharath", "marks": 90},
    "102": {"name": "Rahul", "marks": 85},
    "103": {"name": "Anitha", "marks": 92}
}

b = input("enter student ID")

if b in students:
    print("name :",students[b]["name"])
    print("marks" ,students[b]["marks"])
    
else:
    print("student ID not found")