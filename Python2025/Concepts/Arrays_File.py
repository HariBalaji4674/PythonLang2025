# array is fixed size
# help()

import array
import pyspark as pk
from operator import index

arr = array.array('i',[1,2,3,4,5])
print(arr)

"""
arr = array.array('a',[1,2,3,4,5])
ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
"""
# pk.Union(123,123)
def linear_search(arr,target):
    size = len(arr)
    for i in range(0,size):
        if arr[i] == target:
            return i
    return -1


list1 = [23,45,67,89,32,10]
target = 10
result = linear_search(list1,target)
print(result)


print(7/2) # Returns Float Normal Division
print(7//2) # Returns Integer Floor Division

"""
1: SQL
2: Python
3: R-Programming
4: Apache Kafka
5: Apache Spark
6: Hadoop
7: AWS/Azure/GCP
8: Snowflake DB 
Rounds of Interviews

1: SQL Round
2: System Design 
3: Data Modelling

"""

