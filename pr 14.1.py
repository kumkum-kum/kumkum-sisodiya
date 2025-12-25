import datetime 
import time
import math
import random
import string
import uuid

class studentmodule():
                def datetime_menu(self):
                    while True:
                        print("\nDatetime and Time operations:")
                        print("1.Display current data and time")
                        print("2.Calculated difference between two dates/time")
                        print("3.Format data into custom format")
                        print("4.Stopwatch")
                        print("5.Countdown Timer")
                        print("6.Back to main menu")

                        a = int(input("Enter your choice for datatime and time operations:"))

                        if a==1:
                            now = datetime.datetime.now()
                            
                            b = now.strftime("%Y-%m-%d  %H:%M:%S")
                            print(f"Current Data and Time:{b}")

                        elif a==2:
                            x = datetime.datetime.strptime(input("Enter the first date(YYYY-MM-DD):"),"%Y-%m-%d")
                            y = datetime.datetime.strptime(input("Enter the second date(YYYY-MM-DD):"),"%Y-%m-%d")
                            
                            print(f"Difference :{abs((x-y).days)}days")

                        elif a==3:
                            now = datetime.datetime.now()
                            
                            c = now.strftime("%A,%B %d,%Y")
                            print(f"Current Data and Time:{c}")

                        elif a==4:
                            input("Enter to start time :")
                            start = time.time()
                            input("Enter to end time :")
                            end = time.time()
                            print(f"Time stop:{round(end-start,2)}seconds")

                            # print("Start")
                            # time.sleep(2)  
                            # print("End after 2 seconds")
                        
                        elif a==5:
                            second = int(input("Enter second for countdown:"))
                            for i in range(second,0,-1):
                                print(i,end="...")
                                time.sleep(1)
                            print("time up")
                        
                        elif a==6:
                            break

                        print("===========================")

                def math_menu(self):
                     while True:
                          print("\nMathematical Operations:")
                          print("1.Calculated Factorial")
                          print("2.Solve Compound Interest")
                          print("3.Trigometric Calculation")
                          print("4.Area of Geomertic shapes")
                          print("5.Back to main menu")

                          a = int(input("Enter your choice for mathematical operations:"))

                          if a==1:
                               number = int(input("Enter the number:"))
                               print(f"Factorial :{math.factorial(number)}")

                          elif a==2:
                               p = float(input("Enter principal amount:"))
                               r = float(input("Enter rate of interest:"))
                               y = float(input("Enter year:"))

                               amount = p*(1+r/100)**y
                               print(f"Compound Interest:{amount:.2f}")

                          elif a==3:
                               x= int(input("enter the value:"))

                               angle = math.radians(x)
                               print(f"sin:{math.sin(angle)}")
                               print(f"cos:{math.cos(angle)}")
                               print(f"tan:{math.tan(angle)}")

                          elif a==4:
                               print("\n Geometric Shape:")
                               print("1.circle")
                               print("2.rectangle")

                               shape = int(input("Select Shape:"))
                               if shape ==1:
                                    radius = float(input("enter the value of radius:"))
                                    
                                    area = math.pi * (radius**2)
                                    print(f"Area of Circle:{area}")
                               
                               elif shape==2:
                                    l = float(input("Enter the length value:"))
                                    w = float(input("Enter the width value:"))

                                    area = l*w
                                    print(f"Area of Reactangle:{area}")
                                

                          elif a==5:
                            break

                          print("===========================")


                def random_menu(self):
                     while True:
                          print("\nRandom Data Generation:")
                          print("1.Generate Random Number")
                          print("2.Generate Random List")
                          print("3.Create Random Password")
                          print("4.Generate Random OTP")
                          print("5.Back to main menu")

                          a = int(input("Enter your choice for Random data generation:"))

                          if a==1:
                               
                               number = [random.randint(1,100) ]
                               print(f"Random Number:{number}")

                          elif a==2:
                               list = int(input("Enter the random list number:"))

                               list = [random.randint(1,100)]
                               print(f"Random List:{list}")

                          elif a==3:
                               length = int(input("Enter password length:"))

                               char = string.digits + string.ascii_letters 
                               password = ''.join(random.choice(char)for i in range(length))
                               print(f"Random Password:{password}")

                          elif a==4:
                               otp_list = [random.choice(string.digits)for _ in range(6)]
                               otp = ''.join(otp_list)
                               print(f"Random OTP:{otp}")

                          elif a==5:
                               
                            break

                          print("===========================")

                def uuid_menu(self):
                     uuid_id = uuid.uuid4()
                     print(f"Generated UUID:{uuid_id}")
                     print("===========================")

                def file_menu(self):
                     while True:
                          print("\nFile Operation:")
                          print("1.Create a new file")
                          print("2.Write to a file")
                          print("3.Read from a file")
                          print("4.Append to a file")
                          print("5.Back to main menu")

                          a = int(input("Enter your choice for File operation:"))

                          if a==1:
                               filename = input("Enter file name:")

                               try:
                                    file = open(filename,"x")
                                    print("File created successfully!")
                                    file.close()

                               except FileExistsError:
                                    print("File does not exit")

                          elif a==2:
                               filename = input("Enter file name:")
                               write = input("Enter data to write:")
                               file = open(filename,"w")
                               file.write(write)
                               print("Data written successfully!")
                               file.close()

                          elif a==3:
                               filename = input("Enter file name:")
                               file = open(filename,"r")
                               content = file.read()
                               print("File content:")
                               print(content)
                               file.close()

                          elif a==4:
                               filename = input("Enter file name:")
                               append = input("Enter data to append:")
                               file = open(filename,"a")
                               file.write("\n" + append)
                               print("Data append successfully!")
                               file.close()

                          elif a==5:
                               
                            break

                          print("===========================")

                def module_menu(self):
                     
                     print("Explore Module Attribute:")
                     module = input("Enter module name to explore:")

                     if module == "math":
                          attributes = dir(math)
                          print(f"Available Attribute in {module}module:")
                          print(attributes[:20],"....")
                          print("=====================")

                     else:
                          print("Module not found ")

enter = studentmodule()



print("=======================================")
print("Welcome to Multi =Utility Toolkit")
print("========================================")

while True:
    print("\n Choose an option:")
    print("1.Datatime and Time operations")
    print("2.Mathematical operations")
    print("3.Random Data Generation")
    print("4.Generate Unique Identifier(UUID)")
    print("5.File operations (Custom Module)")
    print("6.Explore Module Attribute(dir()")
    print("7.Exit")
    print("====================================")

    a = int(input("Enter your choice:"))

    if a==1:
         enter.datetime_menu()
    elif a==2:
         enter.math_menu()
    elif a==3:
         enter.random_menu()
    elif a==4:
         enter.uuid_menu()
    elif a==5:
         enter.file_menu()
    elif a==6:
         enter.module_menu()
    elif a==7:
         print("===============================")
         print("Thank you for using the Multi-Utility Toolkit!")
         print("===============================")

         break
    

    else :
         print("\n Invaild option")
                               
                               
                               
                               
                               


                          



                               

                                    

                               
                     











































