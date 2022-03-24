msg = input()
msg_in = input()
n = 30
help = ''


for i in range(26):

    for j in range(len(msg_in)):
        if ord(msg_in[j]) + i > 90:
            help += chr(64 + (ord(msg_in[j])+i) % 90)
        else:
            help += chr(ord(msg_in[j]) + i)

    if msg.find(help) != -1 or msg == help:
        n = i
        break

    help = ''


if n == 30:
    print('IMPOSSIBLE')
else:
    help = ''

    for i in range(len(msg)):
        if ord(msg[i]) - n < 65:
            help += chr(90-(64-(ord(msg[i])-n)))
        else:
            help += chr(ord(msg[i])-n)

    print(help)
