print("Peddireddy Hari Vardhan Reddy")


"""
Conditional Statements
if
else
else-if
"""

if False:
    print("Peddireddy")
else:
    print("Hari Vardhan Reddy")

height = 2

if height > 10:
    print("Ticket Is Required")
else:
    print("No Ticket Is Required")

age = 10

if age >=10:
    print("Go to Next if loop")
    if age == 10:
        print("Hey There your age is 10 Can you wait for some more months")
else:
    print("Please wait for some more time")

number = int(input("Please enter the number : "))

if number % 2 == 0:
    print(f"{number}  is even number")
else:
    print(f"{number} is not even number")

height = int(input("Please enter your heighr : "))
age = int(input("Please enter your age :  "))
amount = int(input("please enter your amount : "))

if height > 3 :
    print("You can ride ")
    if age < 12:
        print("please pay 150 rs")
    elif age <= 18:
        print("please pay 250 rs")
else:
    print("Please enter 300 rs")

"""
Leap Year Or Not
check : If the number is divisble by 4
divisible by 4 :
    divisible by 100:
        divisible by 400
        not divisible by 400 not a leap year
"""
year = int(input("Please Enter the year : "))

if year % 4 == 0:
    print("Please Check with 100 amd 400")
    if year % 100 == 0:
        print("Please check with 400 ")
        if year % 400 == 0:
            print(f"Congratulations {year} is a leap year")
        else:
            print("Sorry !!! This is not leap")
    else:
        print(f"Congratulations {year} is a leap year")
else:
    print("Sorry !!! This is not leap")

print(year % 100 == 0)