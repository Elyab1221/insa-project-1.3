import time
username=input("enter a user name: ")
password=input("enter your password: ")
attempt=0
while attempt<=5:
    if username=="admin" and password=="admin123":
        print("access granted")

        # k = input("enter your name: ")

        l=-1

        try:
            l = float(input("enter your marks in sub1: "))
        except ValueError:
            print("please enter a valid number")

        while l > 100 or l < 0:
            try:
                l = float(input("please enter your actual marks in sub1: "))
            except ValueError:
                print("please enter a valid number")
        m=-1
        try:
            m = float(input("enter your marks in sub2: "))
        except ValueError:
            print("please enter a valid number")

        while m > 100 or m < 0:
            try:
                m = float(input("please enter your actual marks in sub2: "))
            except ValueError:
                print("please enter a valid number")
        n=-1
        try:
            n = float(input("enter your marks in sub3: "))
        except ValueError:
            print("please enter a valid number")

        while n > 100 or n < 0:
            try:
                n = float(input("please enter your actual marks in sub3: "))
            except ValueError:
                print("please enter a valid number")
        average = (l + m + n) / 3
        print("                  ")
        print("     Report-Card "      )
        print("                  ")
        print( "========================================== ")
        print("your name is: ", username)
        print("your average marks is: ", average)
        if average >= 80 and average <= 100:
            print("your grade is A")
        elif average >= 70 and average <= 79:
            print("your grade is B")
        elif average >= 60 and average <= 69:
            print("your grade is C")
        elif average >= 50 and average <= 59:
            print("your grade is D")
        else:
            print("your grade is F")

        if average >= 50:
            print("you have passed")
        else:
            print("you have failed")

        break
    else:
        attempt+=1
        print("incorrect credentials")
        print("you have attempted ", attempt, " times")
        if attempt==1:
            print("after yor 5th fail your account will be locked")
            print("wait for 5 seconds")
            time.sleep(5)  
        elif attempt==2:
            print("after yor 5th fail your account will be locked")
            print("wait for 10 seconds")
            time.sleep(10)
        elif attempt==3:
            print("after yor 5th fail your account will be locked")
            print("wait for 20 seconds")
            time.sleep(20)
        elif attempt==4:
            print("after yor 5th fail your account will be locked")
            print("wait for 40 seconds")
            time.sleep(40)
        else:
            print("your account is locked")
            break
        username=input("enter a user name: ")
        password=input("enter your password: ")
exit()