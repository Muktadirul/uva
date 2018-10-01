T = int(input())
for i in range(1,T+1):
    test_case = input()
    players = list(map(int, test_case.split()))
    # players.sort()
    print("Case "+str(i)+":",players[int(len(players[1:])/2)+1])
