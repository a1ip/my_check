

def recall_password(grid,
                    password,
                    count=4):
    if count:
        psw = ""
        for i in range(4):
            #deciphering first iteration
            for g,p in zip(grid[i],
                           password[i]):
                if g == "X":
                    psw += p
        return (psw +
                recall_password( #recursion calling with rotated grid
                    tuple(zip(*reversed(grid))), #rotating 90° CW
                    password,
                    count - 1)
                )
    else:
        return ""
        


if __name__ == "__main__":
    assert recall_password(
    ('X...',
    '..X.',
    'X..X',
    '....'),
    ('itdf',
    'gdce',
    'aton',
    'qrdi')) == 'icantforgetiddqd', "prvni"

    assert recall_password(
    ('....',
    'X..X',
    '.X..',
    '...X'),
    ('xhwc',
    'rsqx',
    'xqzz',
    'fyzr')) == 'rxqrwsfzxqxzhczy', "druha"


