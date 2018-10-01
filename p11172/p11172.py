output = ['>','<','=']
test_case = input()
for i in range(0, int(test_case)):
    list_of_numbers = input()
    numbers = list(map(int, list_of_numbers.split()))
    if  numbers[0] > numbers[1] :
        print(output[0])
    elif numbers[0] < numbers[1]:
        print(output[1])
    else:
        print(output[2])
