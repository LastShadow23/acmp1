import re

marks = "-,.?!=:'"

prgh = []

with open("INPUT.TXT", "r") as file:
    w, b = map(int, file.readline().split())

    # get paragraphs from text
    el = ""
    for line in file:

        if line == '\n':
            prgh.append(el)
            el = ""
            continue

        # add extra spaces to punctuation mark symbol
        for mark in marks:
            line = line.replace(mark, mark + " ")

        el += line

    prgh.append(el)

indent = " " * (b - 1)  # one less

tmp = []
words = []
word_pttrn = re.compile(f"[{marks}\w]+")

for el in prgh:

    if not el:
        continue

    # divide paragraphs into list of words
    tmp = re.findall(word_pttrn, el)

    i = 1
    while i < len(tmp):
        word = tmp[i]

        if word in marks:
            # concat words and marks in the list
            tmp[i - 1] += tmp.pop(i)
            i -= 1
        i += 1

    # add nextline symbol after paragraph
    # and extend our words-list
    tmp.append("\n")
    words.extend(tmp)

# build result text string
res_text = ""
buf = indent
cur_len = len(indent)
for word in words:

    if word == "\n":
        res_text += buf + "\n"
        buf = indent
        cur_len = len(indent)
        continue

    if cur_len + len(word) + 1 > w:
        res_text += buf + "\n"
        buf = word
        cur_len = len(buf)
    else:
        buf += " " + word
        cur_len += 1 + len(word)

with open("OUTPUT.TXT", "w") as file:
    file.write(res_text)

