from array import *

_array = array('i') # i = int = integer
_product = 1
_sum = 0
 
_array = input().split() # split() slice string into an array of strings

for i in range(len(_array)):   # for each element in array
    e = int(_array[i])
    if i % 2 == 0:
        _sum += e
    if e % 3 != 0:
        _product *= e
        

print("сумма:", _sum)
print("произведение:", _product)