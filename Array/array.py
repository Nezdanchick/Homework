from array import *

_array = array('i') # i = int = integer
 
_array = input().split(',') # split() slice string into an array of strings
# массив = array

i = 0 # iterator
for e in _array:   # for each element in array

    isNull = False # for clear strings

    # 3)    
    if e.strip() == "": # strip() deletes all spaces and tabs from string
        print("пустой элемент -", i + 1, '\n')
        isNull = True

    if isNull == False:
        # 1)
        if (i % 2) == 1:
            print("четный элемент -", e, '\n')

        # 2)
        if (int(e) % 3) != 0:
            print("не кратное 3-м -", e, '\n')
    
    # i increase
    i += 1