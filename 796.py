list_of_lines = []
text = []
punctuation = [',', '.', '?', '!', '-', ':', "'"]


with open("input.txt", "r") as f:

    while True:
        line = f.readline()

        while " " * 2 in line:
            line = line.replace(" " * 2, " ")

        for index in punctuation:
            line = line.replace(" " + index, index)

        if not line:
            break

        list_of_lines.append(line)

w, b = (map(int, list_of_lines[0].split()))
list_of_lines.pop(0)
indent = ' ' * b
list_of_lines[0] = indent + list_of_lines[0]

for num, line in enumerate(list_of_lines):

    for index in punctuation:

        for i, check in enumerate(line):
            if check == index and i + 1 < len(line):
                if line[i+1] == " " or line[i + 1] in punctuation:
                    continue
                else:
                    line = line[:i] + index + " " + line[i + 1:]

    if line == '\n' or line == indent + '\n':
        if num + 1 < len(list_of_lines):
            list_of_lines[num + 1] = indent + list_of_lines[num + 1]
    else:
        text.append(line.rstrip('\n').rstrip())

text_new = " ".join(text).split("     ")

skip = 0

for line in text_new:
    line = indent + line.strip()
    count = 0
    start = 0
    iterr_line = list(line)

    while count != len(iterr_line):
        if iterr_line[count] == " ":
            if count - start >= w:
                if iterr_line[count+1] == " ":
                    skip = count
                    continue
                else:
                    iterr_line[skip] = "\n"
                    start = skip
            skip = count

        count += 1
    print("".join(iterr_line))




