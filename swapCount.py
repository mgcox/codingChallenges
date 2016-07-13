t = int(raw_input())

for i in range(0,t):
    numOfPlates = int(raw_input())

    plateArr = map(int, raw_input().split())

    for index,plate in enumerate(plateArr):
        if index > 0 && plate < plateArr[index-1]:
            temp = plate
            plate = plateArr[index - 1]
            plateArr[index - 1] = temp
        