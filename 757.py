a = input()

C, H, O = [int(i) for i in a.split(' ')]
atom = [C // 2, H // 6, O]

print(min(atom))