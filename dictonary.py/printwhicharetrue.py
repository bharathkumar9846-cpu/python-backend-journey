users = [
    {"username": "bharath", "active": True},
    {"username": "rahul", "active": False},
    {"username": "anitha", "active": True}
]


for i in users:
    if i.get("active") == True:
        print(i.get("username"))
print()