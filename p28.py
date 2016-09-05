d = [1]
n = 2
for i in range(500):
    for j in range(4):
        d.append(d[-1] + n)
    n += 2

print(sum(d))


