def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - get_value(game[i-1])
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            result += get_value(game[i + 1])
            if game[i].upper() == 'X':
                if game[i + 2] == '/':
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        if in_first_half:
            in_first_half = False
            if game[i].upper() == 'X':
                in_first_half = True
                frame += 1
        else:
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char in ('123456789'):
        return int(char)
    elif char in ('/Xx'):
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()