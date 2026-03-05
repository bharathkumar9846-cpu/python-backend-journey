phonebook = {
    "Rahul" : 98765,
    "Anitha" : 91234,
    "Bharath" : 99887
}

a = input("enter name")
if a in phonebook:
    print(phonebook.get(a))
else:
    print("Contact not found")
    
b = input("Do you want to add a new contact? (yes/no)").lower()
if b == "yes":
    name_ = input("enter name")
    number = int(input("enter number"))
    phonebook.update({name_ : number})
   
print(phonebook)