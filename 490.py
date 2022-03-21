from datetime import datetime

data1 = input()
data2 = input()

d1, m1, y1 = [int(i) for i in data1.split('.')]
d2, m2, y2 = [int(i) for i in data2.split('.')]

a = datetime(y1+1900, m1, d1)
b = datetime(y2+1900, m2, d2)
c = b - a
print(c.days)
