while True:

    test_case = input()
    if int(test_case) > 0:
        raw_center = input()
        center = list(map(int, raw_center.split()))
    else:
        break

    for i in range(0, int(test_case)):
        raw_coordinate = input()
        coordinate = list(map(int, raw_coordinate.split()))
        if center[0] == coordinate[0] or center[1] == coordinate[1]:
            print('divisa')

        elif center[0] < coordinate[0]:
            if center[1] > coordinate[1]:
                print('SE')
            else:
                print('NE')
        elif center[0] > coordinate[0]:
            if center[1] > coordinate[1]:
                print('SO')
            else:
                print('NO')
