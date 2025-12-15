print("---Python OOP Project: Employee Mangement System---")


class person():
     def __init__(self,name,age):
        self.name = name
        self.age = age 

    
class employee(person):
     def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.salary = salary

     def __del__(self):
                 print(f"{self.employee_id},{self.name},{self.age},{self.salary}employee Destroyed!")

     def set_salary(self, salary):  
                self.salary = salary
            
     def set_employee_id(self,employee_id):
                self.set_employee_id = employee_id

     def get_salary(self):  
                return self.salary
                
     def get_employee_id(self):
                return self.employee_id
           
# print( "employee_id: ", employee.get_employee_id())  
# employee.set_employee_id("B456")
# print( "employee_id :",employee.get_employee_id())  

# print("salary: " ,employee.get_salary())
# employee.set_salary("40000")
# print("salary: " ,employee.get_salary())
     

        
    
class manager(employee):
     def __init__(self,name ,age,salary,employee_id,department):
        super().__init__(name,age,salary,employee_id)
        self.department = department

while True:
    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    a = int(input("\nEnter your choice : "))  

    if a==1:
          name= input("\nEnter name:")   
          age = int(input("Enter age:"))  
          person1 = person(name,age)

          print(f"\nPerson created with name:{name} and age:{age}")

          print("\n---Choose another opertion---")   

    elif a==2:
         name= input("\nEnter name: ")
         age = int(input("Enter age:"))
         employee_id = input("Enter employee ID:")
         salary = int(input("Enter salary:"))

         employee1 = employee(name,age,employee_id,salary)

         print(f"\nEmployee created with name: {name}, age:{age}, ID: {employee_id}, and salary: {salary}")

         print("\n---Choose another opertion---")

    elif a==3:
         name= input("\nEnter name: ")
         age = int(input("Enter age:"))
         employee_id = input("Enter employee ID:")
         salary = int(input("Enter salary:"))
         department = input("Enter department :")

         manager1 = manager(name,age,employee_id,salary,department)
        
         print(f"\nManager created with name: {name}, age:{age}, ID: {employee_id}, salary: {salary},and Department: {department}")
          
        
         print("\n---Choose another opertion---")

    elif a==4:
        
        print("\n choose details to show:")
        print("1.person")
        print("2.employee")
        print("3.manager")

        b = int(input("Enter your choice :"))

        if b==1:
         print(f"\nname:{person1.name} \nage:{person1.age}") 

        elif b==2:
          print(f"\nname: {employee1.name},\nage:{employee1.age},\nID: {employee1.employee_id},\nsalary: {employee1.salary}")   
        
        elif b==3:
          print(f"\nname: {manager1.name}, \nage:{manager1.age}, \nID: {manager1.employee_id}, \nsalary: {manager1.salary},\nDepartment: {manager1.department}")

          break
        else:
              print("Invaild option")    

    elif a==5:
          print("\nExiting the system . All resource have been freed")  

          print("\n Goodbye!")

          break

    else:
          print("\n Invaild option") 




               

            


            
        

            

            




        


            

            
    

    

        


