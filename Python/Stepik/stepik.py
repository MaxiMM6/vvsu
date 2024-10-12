n = int(input())

res = []
count = 0

for i in range(n):
    l = int(input())
    count += l
    res.append(count)
    l = count
print(res[1:])

