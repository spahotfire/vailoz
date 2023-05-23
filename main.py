studentid = []
studentname = []
studentdob = []
def addstudent():
   """
   Student id, name, Dob
   studentid.append(id)
   """
   numofstudents = int(input("How many student u wanna add: "))
   i = 0
   if not i > 0:
      print("error")
   else:
      while i < numofstudents:
         id = int(input(f"Input the ID of student {i+1}:"))
         studentid.append(id)
         name = str(input(f"Input the Name of student {i + 1}:"))
         studentname.append(name)
         dob = int(input(f"Input the dob of student {i + 1}:"))
         studentdob.append(dob)
         i = i + 1

   # Limite the number of input student (No negative number and no 0)
def deletestudent():
   iddel = int(input(" ID u wanna delete: "))
   for a in studentid:
      if a == iddel:
         a = studentid.index(iddel)
         studentname.pop(a)
         studentid.pop(a)
         studentdob.pop(a)
         print("Success")
      else:
         print("error")
   return

   # Show and error when the student id isn't match

def showstudent():
   i = 0
   a = len(studentid)
   if not studentid:
      print("error")
   else:
      while i< a:
         print(f"{studentid[i]}. {studentname[i]} {studentdob[i]}")
         i = i + 1
   return
   # Error when list is empty

def findstudent():
   idfind = int(input("Input the ID student u wanna find: "))
   for a in studentid:
      if a == idfind:
         a = studentid.index(idfind)
         print(f"{studentid[a]}. {studentname[a]} {studentdob[a]}")
      else:
         print("error")
      return
      # Error when no match student
   
while True:
   print("1. Add student")
   print("2. Delete")
   print("3. Show student")
   print("4. Find student")
   print("5. Exit program")
   a = int(input("What would you like to do? "))
   match a:
      case 1:
         addstudent()
      case 2:
         deletestudent()
      case 3:
         showstudent()
      case 4:
         findstudent()
      case 5:
         break