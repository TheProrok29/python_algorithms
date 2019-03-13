def sum(list):
    if list == []:
        return 0
    else:
        return list[0] + sum(list[1:])