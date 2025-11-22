print("welcome to the pattern generator and number analyzer !")

while True:
     print()
     print("select the option")

     print("1. generate a pattern")
     print("2. analyzi a range of number")
     print("3. exit")

     a = int(input("enter your choice"))

     if a==1:
          b= int(input("enter the number of rows for pattern"))
          for i in range(1, b+1):
               for j in range(i):
                    print("*", end="")
          print()

     elif a==2:

         x = int(input("enter the start of the range"))
         y = int(input("enter the end of the range"))

         print()
         sum=0
         for i in range(x,y+1):
              if i%2==0:
                  print(f"number{i}is even")
              else:
                  print(f"number{i}is odd")

         sum+=i
         print()

         print(f"sum of all number from {x} to {y}is :{sum}")
     
         print()
     elif a==3:
        print("exiting the program goodbye!")

        break
   
     else:
         print("invaild the option")






 

     


                

       
            
        


