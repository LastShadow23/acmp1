a = input()

C, H, O = [int(i) for i in a.split(' ')]
Atom = [C // 2, H // 6, O]

print(min(Atom))