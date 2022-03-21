with open('INPUT.TXT', 'r') as f:
    A = [int(i) for i in f.read().split(' ')]
    S = 2 * A[2] * (A[0] + A[1])
    if S % 16 == 0:
        paint = S // 16
    else:
        paint = S // 16 + 1

with open('OUTPUT.TXT', 'w') as f:
    f.write(str(paint))