a = input()

ball = [1, 2, 3]

for i in a:
    if i == 'C':
        ball[0], ball[2] = ball[2], ball[0]

    elif i == 'A':
        ball[0], ball[1] = ball[1], ball[0]

    elif i == 'B':
        ball[2], ball[1] = ball[1], ball[2]

print(ball.index(1)+1)
