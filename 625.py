my_dict = {}
full_dict = {}
key = 0
press = 0

for i in range(1, 10):
    my_dict.clear()
    key += 1
    s = input()
    click = 0
    for letter in s:
        click += 1
        my_dict[letter] = my_dict.get(letter, {'click': click, 'key': key})
        full_dict.update(my_dict)

msg = input()

up_index = False
temp_up_index = True
key_num_old = 50

for a in msg:
    if a == ' ':
        press += 1
        key_num_old = 50
        continue

    if full_dict.get(a, None):
        if full_dict.get(a).get('key') == 1:
            click_num = full_dict.get(a).get('click')
            key_num = 1
            if key_num_old == key_num:
                press += 1
            key_num_old = key_num
            press += click_num
            if not up_index:
                temp_up_index = True
            continue

    if not full_dict.get(a, None):
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

    click_num = full_dict.get(a).get('click')
    key_num = full_dict.get(a).get('key')

    if key_num_old == key_num:
        press += 1

    key_num_old = key_num
    press += click_num

print(press)

