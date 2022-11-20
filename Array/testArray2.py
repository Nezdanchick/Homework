A = input().split()
s=0
for i in range(len(A)):
    if int(A[i]) >= 10 and int(A[i]) % 2 == 1:
        s += int(A[i])
print(s)