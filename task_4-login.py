import time
username=input("enter a user name: ")
password=input("enter your password: ")
attempt=0
while attempt<=5:
    if username=="admin" and password=="admin123":
        print("access granted")
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