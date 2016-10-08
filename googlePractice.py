import time

def solution(X):
    #Cast to string
    stringVersion = str(X)
    length = len(stringVersion)

    newString = []
    

    for i in range(0,length-1):
        if stringVersion[i] < stringVersion[i+1]:
            newString.append(i+1)
        else:
            newString.append(i)

    for j in newString:
        print ("%d", j)

solution(1123)

print(str(time.time()))