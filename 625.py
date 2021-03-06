keyboard = {}

for key in range(1, 10):
    for click, char in enumerate(input(), 1):
        keyboard[char] = {"click": click, "key": key}

msg = input()

up_index = False
temp_up_index = True
key_num_old = 10
press = 0

for a in msg:
    if a == ' ':
        press += 1
        key_num_old = 10
        continue

    if a in ('.', '!', '?'):
        click_num = keyboard[a]['click']
        key_num = keyboard[a]['key']
        if key_num_old == key_num:
            press += 1
        key_num_old = key_num
        press += click_num
        if not up_index:
            temp_up_index = True
        continue

    if not keyboard.get(a):
        if temp_up_index:
            a = a.lower()
            temp_up_index = False
        else:
            if not up_index:
                press += 1
                up_index = True
                a = a.lower()
            else:
                a = a.lower()
    else:
        if up_index or temp_up_index:
            up_index = False
            temp_up_index = False
            press += 1

    click_num = keyboard[a]['click']
    key_num = keyboard[a]['key']

    if key_num_old == key_num:
        press += 1

    key_num_old = key_num
    press += click_num

print(press)
