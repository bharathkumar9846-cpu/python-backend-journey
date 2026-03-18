student = {
    "name" : "bharath",
    "age"  : 21,
    "city":" bangalore"
}

student["age"] = 22
student["grade"] = "A"
for key, value in student.items():
    print(key, ";" , value)