import os


def display(mp):
    for i in range(3):
        for j in range(3):
            if mp[i][j] == ' ':
                print((i*3 + j)+1, end='')
            else:
                print(mp[i][j], end='')

            if j != 2:
                print(end=' | ')
        print()


def validate(mp):
    for i in range(3):
        if mp[i][0] == mp[i][1] == mp[i][2] and mp[i][0] in ('x', 'o'):
            return mp[i][0]

        if mp[0][i] == mp[1][i] == mp[2][i] and mp[0][i] in ('x', 'o'):
            return mp[0][i]

    if mp[0][0] == mp[1][1] == mp[2][2] and mp[0][0] in ('x', 'o'):
        return mp[0][0]
    
    if mp[0][2] == mp[1][1] == mp[2][0] and mp[0][2] in ('x', 'o'):
        return mp[0][2]


ph = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9

def x(n):
    return (n-1) // 3

def y(n):
    return (n-1) % 3

turn = 'x'

while 1:
    display(ph)
    t = input("Enter position for {}: ".format(turn))

    try:
        t = int(t)
    except ValueError:
        print("Enter valid integer")
        continue

    if not 1 <= t <= 9:
        print("Enter valid position [1, 9]")

    if ph[x(t)][y(t)] != ' ':
        print("position filled")
        continue

    os.system("cls")

    ph[x(t)][y(t)] = turn

    r = validate(ph)
    if r:
        print("{} wins".format(r))
        display(ph)

        break

    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'
