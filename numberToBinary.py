#Without using bin, convert number to binary

def binNumber(n):
    if n > 1:
        binNumber(n/2)

    print n % 2,


print binNumber(467)