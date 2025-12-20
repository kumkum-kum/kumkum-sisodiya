
import datetime


class journalmanager:
     

        def __init__(self,filename = "journal.txt"):
              self.filename = filename

        def add_entry(self):
              try:
                    enter = input("\nenter your journal entry:")
                    with open ("journal.txt","a")as file:
                          file.write(enter + "\n")
                    with open("journal.txt","r")as file:
                          print(file.read())
                    print("\n Entry added successfully!")
                

              except FileNotFoundError:
                    print("file does not exist!")

        def view_entry(self):
             try:
               
               print("\nYour journal enties:")
               print("---------------------")
     
               print("\noutput (if file exists)")
               now = datetime.datetime.now()

               formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
               print( formatted_date)

               file = open("journal.txt", "r")  
               print(file.readlines())
          

               
               now = datetime.datetime.now()

               time = now.strftime("%d-%m-%Y %H:%M:%S")
               print( time)

               file = open("journal.txt", "w") 
               file.write("\nhad a great session on oops concept")
            
               file.close()
               

              

             except FileExistsError:
                 print("\noutput (if file does not exits)")
                 print("no journal enties")

               


        def serach_entry(self):
               
               keyword = input("\nenter a keyword or date to serach:")
               try:
                     with open ("journal.txt","r")as file:
                           lines = file.readlines()
      
                           matches = [line.strip()for line in lines ]
                           if matches:
                                 print("\nOutput(if a match is found ):")
                                 print("matching entries:")
                                 print("-------------------")
                                 for entry in matches:
                                       print(entry)
                                       now = datetime.datetime.now()
                                       
                                       formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
                                       print( formatted_date)
                           else:
                                 print("\nOutput(if no match is found):")
                                 print(f"No entries were found for the keyword:{keyword}")
               except FileNotFoundError:
                     print("file does not found error")

        def delete_all_entry(self):
              try:
                    with open ("journal.txt","r")as file:
                       print(file.read())

                    confirm = input("\nare you sure you want to delete all enties?(yes/no):")

                    if confirm == "yes":
                          print("\nAll journal enties have been deleted ")
                    else:
                          print("\nDeletion cancelled")
              except FileNotFoundError:
                    print("\nNo journal enties delete")  

        def view_journal(self):
              try:
                    with open("jouranl.txt","r")as file:
                          print(file.read())
              except FileNotFoundError:
                    print("\nOutput:\nError:The journal file does not exist.please add a new entry first")

        def invaild_input(self):
              try:
                    with open("journal","r")as file:
                          print(file.read())
              except FileNotFoundError:
                    print("\nOutput:\nInvaild option.please select a vaild option from the menu")


            




           

entry = journalmanager()
            

print("Welcome to personal journal manager !")
while True:
    print("\nplease select an option:")
    print("\n1.Add a new enter")
    print("2.View all entries")
    print("3.Search for an entry")
    print("4.delete all entries")
    print("5.Handle file not found error")
    print("6.Invaild option")
    print("7.Exit")

    a = int(input("User input:"))

    if a==1:
          entry.add_entry()
    elif a==2:
          entry.view_entry()
    elif a==3:
          entry.serach_entry()
    elif a==4:
          entry.delete_all_entry()
    elif a==5:
          entry.view_journal()
    elif a==6:
          entry.invaild_input()
    elif a==7:
          print("\nOutput:\nThank you for using personal journal manager.Goodbye!")

          break
    else:
          print("\nInvaild option")


                        
                            
