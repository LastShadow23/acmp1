a = input()
k = int(a[:2]) - 1
s = a[2::].replace(" ", "")

s = s[:k:] + s[k+1::]

print(s)
