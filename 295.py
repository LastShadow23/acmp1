msg = input()
msg_in = input()
MAX_SHIFT = 26
MAX_ABC = 90
MIN_ABC = 64
shift = 30
help = ''

for offset in range(MAX_SHIFT):

    for char in msg_in:
        if ord(char) + offset > MAX_ABC:
            help += chr(MIN_ABC + (ord(char) + offset) % MAX_ABC)
        else:
            help += chr(ord(char) + offset)

    if msg.find(help) != -1 or msg == help:
        shift = offset
        break

    help = ''

if shift == 30:
    print('IMPOSSIBLE')
else:
    help = ''

    for char in msg:
        if ord(char) - shift <= MIN_ABC:
            help += chr(MAX_ABC - (MIN_ABC - (ord(char) - shift)))
        else:
            help += chr(ord(char) - shift)

    print(help)
