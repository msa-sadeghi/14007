x = [[1,2], [3,4], [5,6,7]]

print(x[0][0])
print(x[0][1])
print(x[1][0])
print(x[1][1])
print(x[2][0])
print(x[2][1])
print(x[2][2])

y = []
if x[0][0] % 2 == 0:
    y.append(x[0][0])
if x[0][1] % 2 == 0:
    y.append(x[0][1])
print(y)