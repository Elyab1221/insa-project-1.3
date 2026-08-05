k = input("enter your name: ")

l = float(input("enter your marks in sub1: "))
while l > 100 or l < 0:
    l = float(input("please enter your actual marks in sub1: "))

m = float(input("enter your marks in sub2: "))
while m > 100 or m < 0:
    m = float(input("please enter your actual marks in sub2: "))

n = float(input("enter your marks in sub3: "))
while n > 100 or n < 0:
    n = float(input("please enter your actual marks in sub3: "))
average = (l + m + n) / 3

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


    