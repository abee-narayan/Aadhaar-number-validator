def validate_uid(uId):
    dMultTable = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
                  [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
                  [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
                  [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
                  [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
                  [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
                  [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
                  [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
                  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
    permTable = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                 [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
                 [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
                 [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
                 [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
                 [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
                 [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
                 [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]

    c = 0
    print("validate_uid:", c, end=":")
    for i in range(12):
        ni = 0
        newC = 0

        if uId[11 - i].isdigit():
            ni = int(uId[11 - i])
        else:
            print()
            return -1
        newC = dMultTable[c][permTable[i % 8][ni]]
        print(newC, end=":")
        c = newC

    print()
    if c == 0:
        return 0
    return -1

# Example usage:
uId = "330039035062"
result = validate_uid(uId)
print("Result:", result)
