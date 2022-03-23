my_dict = {}
full_dict = {}

for key in range(1, 10):
    s = list(input())
    full_dict.update({letter: {"click": click + 1, "key": key} for click, letter in enumerate(s)})

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

    if full_dict.get(a):
        if full_dict[a]['key'] == 1:
            click_num = full_dict[a]['click']
            key_num = full_dict[a]['key']
            if key_num_old == key_num:
                press += 1
            key_num_old = key_num
            press += click_num
            if not up_index:
                temp_up_index = True
            continue

    if not full_dict.get(a):
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

    click_num = full_dict[a]['click']
    key_num = full_dict[a]['key']

    if key_num_old == key_num:
        press += 1

    key_num_old = key_num
    press += click_num

print(press)

