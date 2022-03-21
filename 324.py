with open('INPUT.TXT', 'r') as f:
    a = f.read().split('\n')
    if a == a[::-1]:
        res = 'YES'
    else:
        res = 'NO'

with open('OUTPUT.TXT', 'w') as f:
    f.write(res)
