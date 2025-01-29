name1 = str(input("Please eneter your name 1 : "))
name2 = str(input("Please enter your name 2 : "))

combine_string = name1 + name2
print(combine_string)

lower_case_string = combine_string.lower()
print(lower_case_string)

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t+r+u+e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l+o+v+e

truelove = true + love
print(truelove)

if truelove < 10 or truelove > 90:
    print(f"Your Love Score is {truelove}, You can Live Together")
elif 40 <= truelove <= 50:
    print(f"Your Score is {truelove}, you are alright")
else:
    print(f"Your Love Score is {truelove}")






