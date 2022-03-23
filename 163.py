eq = input()

if eq[0] == 'x':
    print(int(eq[4]) - int(eq[1] + eq[2]))

elif eq[2] == 'x':
    print((int(eq[4]) - int(eq[0])) * (int(eq[1]+'1')))

else:
    print(int(eq[0]) + int(eq[1] + eq[2]))
