def count(list):
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])