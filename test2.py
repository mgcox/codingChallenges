def solution(S):
    totalPathCount = 0
    StringSplit = S.split("\n")

    pathCount = len(StringSplit)

    for path in StringSplit:

        if path.__contains__(".jpeg") or path.__contains__(".gif"):
            print path
            charLength = len(path.strip())
            numOfSpaces = len(path) - charLength
            totalPathCount += charLength
            totalPathCount += numOfSpaces * 4
    print totalPathCount



S = "dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file1.txt\ndir2\n file2.gif"

solution(S)