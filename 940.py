a = input()
k = int(a[:2])
a = a.replace(" ", "")


def remove(string, index):
    s = list(string)
    del s[index]
    del s[0]
    if k > 9:
        del s[0]
    return "".join(s)


print(remove(a, k))
