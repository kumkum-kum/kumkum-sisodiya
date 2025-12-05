print("\nWelcome to the Data Analyzer and Transformer Program")

while True:
    print("\nMain Menu :")

    print("1. Input Data ")
    print("2. Display Data Summary (Built-in function)")
    print("3. Calculate Factorial(Recursion)")
    print("4. Filter Data by Threshold(Lambda function)")
    print("5.Sort Data ")
    print("6.Display Dataset Statistics(Return Multiple Values)")
    print("7.Exit Program")

    a = int(input("enter your choice : "))

    if a==1:
        print("\nStep 1:Input Data ")

        a= int(input("enter your choice :"))

        arr = list(map(int,input("enter data for a 1D aaray (separated by spaces):").split()))
        print(arr)

        print(" \nData has been stored successfully !")


    elif a==2:
        print("\nStep 2: \nisplay Data Summary (Built -in Function)") 
        print("\nData Summary :")

        length = len(arr)
        print(f"- Total elements : {length}")
        maximum = max(arr)
        print(f"-Maximum value : {maximum} ")
        minimum = min(arr)
        print(f"- Minimum value : {minimum}")
        s = sum(arr)
        print(f"- Sum of all values : {s}")
        average = s/length
        print(f"-Average value : {average}")
    
    elif a==3:
        print("\nStep 3 :Calucalte Factorial(Recursion)")

        n = int(input("enter a number to calculate its factorial :"))

        def factorial(n):
            """ this function represent the factorial of a number"""
            if n == 1:
                return 1
            return n * factorial(n-1)
        
        print(f"\nfactorial of {n} is : {factorial(n)}")
        print(factorial.__doc__)
        
    
    elif a==4:
        print("\nStep 4:Filter Data by Threshold (Lambda Function)")

        z = int(input("enter a threshold value to filter out data above this value :"))

        a = list(filter(lambda x:x >= z,arr))

        print(f"\nFiltered Data (value >= {a}):")

    elif a==5:
        print("\nStep 5 : Sort Data ")

        print("\nChoose sorting option:")
        print("1. Ascending")
        print("2. Descending")

        x = int(input("enter your choice :"))
        if x==1: 
            arr.sort()
            print(f"\nSorted Data in Ascending order: {arr}")
        elif x==2:
            arr.sort(reverse = True)
            print(f"\nSorted Data in Descending order: {arr}")

    
    elif a==6:
        print("\nStep 6 : Display Dataset Statistic(Return Multiple Values)")

        print("\nDataset Statistics:")
        
        #maximum
        def maxi():
            """finding the value of maximum  in arr list"""

            
            
            m = arr[0]
            for i in arr[1:]:
              if i > m:
                  m=i
              
            
            print(f"-maximum value:{m} ")
        maxi()
        print(maxi.__doc__)
         
        #minimum
        def mini():
            """ finding the value of minimum in arr list"""

            n = arr[0]
            for i in arr[1:]:
                if i < n :
                    n=i

            print(f"-minimum value: {n}")
        mini()
        print(mini.__doc__)
              
        #sum
        sum = 0
        
        for i in arr:
            sum+=i
            
        print(f"-\nSum of all value: {sum}")

        #average
        total = 0 
        count = 0 
        for i in arr:
            total+=i
            count+=1

        avg = total/count
        print(f"\nAverage value : {avg}")


    elif a==7:
        print("\nStep 7: Exit Program")

        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye! ")

        break

    else:
        print("\nInvaild Option")






