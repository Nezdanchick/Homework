from array import array


from array import *

arr = array('i')

while True:
    read = input()
    if read == "exit":
        break
    arr.append(int(read))
    
for e in arr:
    print(e)