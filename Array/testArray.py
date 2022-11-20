A = [3 * i + 5 for i in range(10)]
p = 1
for i in range(10):
    if i % 2 == 0:
        p *= A[i]
print(p)        