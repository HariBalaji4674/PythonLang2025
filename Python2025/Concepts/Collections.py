print("Peddireddy".lower())

list = [1,2,3,4,4,5,6,7]

print(list)
print(set(list))

mix_list = [1,"pedd",10.123]
print(mix_list)


"""
Collections:

Mutable : Can change
Immutable : cannot change

- Tuple(): which is ordered and unchangeable
  List is immutable
  Written In curly braces
  
Functions in Tuple:
- Only get functions we can do 
- we can't perform addition,subtraction,modify,append 
- convert to list do operations and again change to tuple
- Joining and Combining Tuples are allowed

- Set {} : Unordered and UnIndexed
  - Mutable and Changeable
  - Written in flower braces
  - add will add single item
  - update will do multiple items at a time
  

- Dictionary: {key:value}
  - A Collection unordered and changeable and indexed
  - flower braces and stored in key and value pairs
  - Keys should be unique and values can be duplicate
  - 


- List[]: Collection which is ordered and changeable
  List Is Mutable
  written in square brackets
  When we need to store collection of data
  collection of things enclosed in square brackets and seperated by commas
  in a list counting start from zero
  list can have duplicate values
  negative indexing
  slicing : [start:last:increment/decrement]

append
pop
remove
insert
extend

Random Module:

"""

list1 = [2,5,9,7,4,3,2,1,6,7,12,11,10]

print(list1[2:8: 1])
list1.sort()
print(list1)

if 2 in list1:
    print("Numer is present")
else:
    print("Number is not present")

for i in list1:
    print(i,end=" ")
print()

print("Hari")
print(len(list1))

list1.append(45)
print(list1)

list1.insert(5,78)
print(list1)

list2 = [2,3,4,5]
list3 = ["apple","banana","custard"]

for i in list2:
    list3.append(i)

print(list3)

list3.extend(list1)

print(list3)

MyTyple = (1,2,3,4,5,6)
print(MyTyple)

mydic = {"name":"peddireddy","age":25,"year": 2025}
print(mydic.values())
print(mydic["name"])
print(mydic.get("name"))

mydic["name"] = "akhila"

print(mydic)

for i in mydic:
    print(i)
    print(mydic[i])

if "name" in mydic:
    print("exist")
else:
    print("not exist")

print(len(mydic))

mydic["color"] = "Blue-Yellow"

print(mydic)

mydic.pop("color")
print(mydic)

del mydic["year"]
print(mydic)