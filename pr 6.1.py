print("welcome to the student organizer!")

student =[]

Allsubject=set()

while True:
    print("select the option :")

    print("1. Add student")
    print("2. Display all students")
    print("3.Update student information")
    print("4.Delete student")
    print("5.Display subject offered")
    print("6. Exit")

    a = int(input("enter the choice "))

    if a==1:
        print("enter student details :")
        
        
        studentid= int(input("enter your studentid:"))
        name = input("enter your name :")
        age = int(input("enter your age:"))
        grade = input("enter your grade:")
        dateofbirth = input("enter your dateofbirth:")
        subject = input("subject(comma-sepearted):").split(",")
        students={
            "name":name,
            "age":age,
            "grade":grade,
            "studentID":studentid,
            "dateofbirth":dateofbirth,
            "subject": subject


        }


        student.append(students)

        Allsubject.update(subject)
         



        print(f"student{name} added successfully!")


    elif a==2:

        print("- - - Display all student- - -")

        if not student :
            print("no student found")
           

        else:
            print("all student")
            for i in student:
                print(f"studentid:{i['studentID']}| name:{i['name']}|age:{i['age']}|garde:{i['grade']}|subject:{i['subject']}")

  
        


    elif a==3:
          
          student_ID=input("enter your student id update:")

          for i in student :
              if i['dateofbirth'][0]==student_ID:
               
               print("what you want to update?")
               print("1. age")
               print("2. subject")

               x = input("enter your choice:")

               if x=="1":
                  new_age= int(input("enter your age:"))
                  student["age"]= new_age
                  print("age update successfully")

               elif x=="2":
                  new_subject = input("enter your new  subject(comma_sepeated):").split(",")
                  student["subject"]= new_subject

                  subject.update(new_subject)
                  print("subject added successfully")

               else:
                  print("invaild option")
               break
              
    
                  



    elif a==4:
        
        student_ID= int(input("enter student id to delete:"))

        for i in range(student):
            if studentid[i]['student id'][0]==student_ID:
                del student[i]

                print("student id delet succefully")


            else:
                print("invaild inforamtion")


    elif a==5:
        print("-- Display subject offered--")

        for subject in sorted(Allsubject):
            print(subject)


    elif a==6:
        print("thank you for your inforamtion")

        break


    else:
        ("invaild option")



    

        






        
       

        

    

    



  