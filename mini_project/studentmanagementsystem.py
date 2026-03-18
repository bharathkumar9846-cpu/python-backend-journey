student = {
    "764": {"name" : "bharath" ,
    "marks" : 90  },
    "765" : {"name" : "ravi" ,
    "marks" : 80 },
    "789" : {"name" : "bhanu",
    "marks" : 75}
}

while True:
      print("1: ADD")
      print("2 : view")
      print("3 : search")
      print("4 : delete")
      print("5 : exit")
      choice = int(input("enter number"))
      if choice == 1:
          student_id = input("enter id")
          student[student_id] = {
              "name" : input("enter name"),
          "marks": int(input("enter marks")) 
              
          }
      elif choice == 2:
          for key, value in student.items():
              print(key, " : ", value)
              
      elif choice == 3:
          student_id = input("Student ID")
          if student_id in student:
              print(student[student_id])
          else:
              print("student no found")
      elif choice == 4:
          student_id = input("student ID")
          if student_id in student:
             del student[student_id]
          else:
              print("student not found")
      elif choice == 5:
          print("exit")
          break
      else:
          print("please try again use numbers 1 to 5")