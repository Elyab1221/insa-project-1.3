k = input("enter your name: ")

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
print("     report-card "      )
print("                  ")
print( "========================================== ")
print("your name is: ", k)
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


    