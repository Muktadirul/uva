iteretion = int(input())
while iteretion:


    dataset = input()
    list_of_data = list(map(int, dataset.split()))
    list_of_data.sort()
    cost = list_of_data[0]
    result =[]
    for i in range(1, len(list_of_data)):
        cost = list_of_data[i]+cost
        print(list_of_data[i])
        result.append(cost)
        # print(cost)
    print(sum(result))
    iteretion = int(input())
