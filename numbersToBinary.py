t = int(raw_input())

for num in range(0,t):
    val = int(raw_input())
    for i in range(1,val+1):
        print (bin(i)[2:]),
    print '\n'


