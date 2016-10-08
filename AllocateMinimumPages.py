t = int(raw_input())



for i in range(0,t):
    numberOfBooks = int(raw_input())
    pagesOfEachBook = map(int,raw_input().split())
    students = int(raw_input())

    maxPages = sum(pagesOfEachBook) / students

    print maxPages
    studentPageCount = 0

    studentCount = 0

    counts = []

    for book in pagesOfEachBook:
            if studentPageCount + book > maxPages and studentCount < students -1:
                if studentCount < students - 1:
                    counts.append(studentPageCount + book)
                    print studentPageCount + book
                    studentPageCount = 0
                    studentCount += 1
            else:
                studentPageCount += book


    print(max(counts))
