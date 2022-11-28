from array import *

_array = input().split() # а как  вводится не сказано)))

# не понятно что значит максимальный, будет 3 варианта
print("последний элемент:", _array[-1])

max = 0
ind = 0
for i in range(len(_array)):
    e = _array[i]
    if int(e) > max:
        max = int(e)
        ind = i + 1
print("наибольший элемент:", max)

print("его индекс:", ind)


result = False
for e in _array:
    if int(e[0]) % 3 != 0:
        result = True
print("не кратные 3 элементы существуют, это", result)