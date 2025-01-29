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



