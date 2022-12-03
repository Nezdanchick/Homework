_array = input().split()
_length = len(_array)
_firstCount = _length // 2
_secondCount = _length // 3
_sum = 0
_product = 1

if _length % 2 != 0:
    _firstCount += 1
if _length % 3 != 0:
    _secondCount += 1

for i in range(_length):
    e = int(_array[i])

    if i % 2 == 0:
        _sum += e
    if e % 3 != 0:
        _product *= e

print("Задание 1 (четные индексы):")
print("сумма -", _sum)
print("количество -", _firstCount, "\n")
print("Задание 2 (индексы не кратные 3-ем):")
print("произведение -", _product)
print("количество -", _secondCount)
