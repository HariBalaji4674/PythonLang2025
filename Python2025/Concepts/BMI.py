height = int(input("Please enter your height : "))
weight = int(input("Please enter your weight : "))

BMI = weight / (height**2)
print(round(BMI,2))


a = 10
b = 20

print(a < 10 and b < 20)
print(a > 10 and b <= 20)

"""
Bitwise Operators
- & --> and
  | --> or
  ^ --> XOR -->
  ~ --> Not (compliment) --> Negate with one value higher a=10 ~a=-11
  << --> left shift  --> will increase the value
  >> --> Right Shift --> will decrease the value
"""

print(~a)
print(b^a)

a = a^b
print(a)

b = a - b
print(b)

a = a - b
print(a)

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 2)
print(b >> 2)

"""
identity operators
is 
is not
"""

a = 100
b = 100

print(a is not b)
print(id(a))
print(id(b))


"""
Membership Operators
in if value found return true
not in : if not found return false
"""

name = "peddireddy"
print('t' in name)

"""
round() function

"""

number = 234.1829383912839

print(round(number, 1))


