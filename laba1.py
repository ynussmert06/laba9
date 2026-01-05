c = int(input())
summ = 0
count = 0
for i in range(0, c + 1):
    summ = summ + i
    count += 1
    print(i)
print(summ)
print(count)
print(summ / count)

c = int(input())
v = int(input())
if c > v:
    print(c)
elif v > c :
    print(v)
else :
    print("равны")

n = int(input())
while n > 0:
    n = n - 1
    print(n)

c = int(input())
for i in range(0 , c, 2):
    print(i)
