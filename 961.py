n, m = map(int, input().split())
a = []
b = []
up = ""
low = ""

for i in range(n):
    row = input().split()
    for j in row:
        a.append(j)

input()

for i in range(n):
    row = input().split()
    for j in row:
        b.append(j)

for i in range(n):
    for j in range(m):
        if a[i][j] != "." and a[i][j] != b[i][j]:
            if a[i][j] <= "Z":
                up += a[i][j]
            else:
                low += a[i][j]

print(len(low+up))
print(''.join(sorted(low)) + ''.join(sorted(up)))