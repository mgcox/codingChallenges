
num = int(raw_input())

for i in range(num):
    string1 = raw_input()
    string2 = raw_input()

    dict = {}

    start = 0
    for index, i in enumerate(string1):
        dict[i] = index


    furthestVal = len(string1)

    result = True
    for c in string2:
        if dict[c] > furthestVal:
            result = False
            break

        furthestVal = dict[c]

    print(result)