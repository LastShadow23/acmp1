a = input()

L, W, H = [int(i) for i in a.split(' ')]
S = 2 * H * (L + W)
if S % 16 == 0:
    paint = S // 16
else:
    paint = S // 16 + 1

print(paint)
