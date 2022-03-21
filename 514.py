k = int(input())
lvl = 0

while k > 0:
    if k >= lvl + 1:
        lvl += 1
    k -= lvl

print(lvl)
