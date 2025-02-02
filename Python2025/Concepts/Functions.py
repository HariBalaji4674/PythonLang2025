print("Functions Section : ")

"""
functions means set of statements which will perform a task
** User defined Functions

** Global Varibales: Used over all the code
** Local Variables : available within a function

Local Variables will override global variables


"""

def my_func(name):
    print("Pedireddy"+name)

my_func("Hari")

def fun1():
    print("Hari")

print(fun1())

def func2():
    return "Peddireddy"

print(func2())

def addition(a,b,c,d):
    return a*b-c/d

print(addition(1,2,3,4))
print(addition(4,3,2,1))

def subtraction(sub1,sub2):
    return sub1-sub2

print(subtraction(200,100))

global_var = 200

def test_var():
    local_var = 500
    print(local_var)
    print(global_var)

test_var()

num = 400

def test_var1():
    global num1
    num1 = 500
    print(num1)

test_var1()

print("Positional  **args and Keyword Arguments **kwargs")

def pos_arg(i,j=500):
    print(i,j)

pos_arg(10,20)
pos_arg(j= 50,i= 30)
pos_arg(800)

def largest(a,b):
    if a>b:
        print(a,b)
    else:
        print(b,a)


largest(20, 10)

largest(100, 200)



def evenOdd(number):
    if number%2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

evenOdd(20)
evenOdd(40)
evenOdd(50)
evenOdd(56)
evenOdd(67)
evenOdd(87)

def print_number(*args): #positional Arguments
    print(args)

print_number(20,30,40,50,60,"peddireddy")

def print_number(**kwargs):#key-word arguments == key value pairs
    print(kwargs)

# print_number(20,30,40)

# Lamda Functions will only have one expression
# lambda arguments : expression

def addition(a,b):
    return a+b

c = addition(20,40)
print(c)

c = lambda a,b : a+b

print(c(20,100))

addition1 = lambda a : a%2 == 0
print(addition1(20))

# map() applies a function to all items in a list
# map will take two arguments function and iterable
numbers = [2,3,4,5,6,7,8]
list1 = list(map(lambda x : x**2,numbers))

print(list1)

# numbers[5] = [list(input("Please enter numbers: "))]
#
# list1 = list(map(lambda x : x**2,numbers))
# print(list1)

# Filter also takes 2 inputs function and iterable

# list1 = filter(,5)
# print(list1)

students = [
    {"name": "Alice Johnson", "age": 14, "class": "8B"},
    {"name": "Michael Smith", "age": 15, "class": "9A"},
    {"name": "Sofia Martinez", "age": 13, "class": "7C"},
    {"name": "Liam Brown", "age": 16, "class": "10D"},
    {"name": "Emma Wilson", "age": 12, "class": "6A"}
]
print(students[0].keys())

def names_out(peoples):
    return peoples[1].keys(),peoples[1].values()

listnames = names_out(students)
print(listnames)