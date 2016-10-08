#https://www.hackerrank.com/challenges/flipping-bits

#You will be given a list of 32 bits unsigned integers. You are required to output the list of the unsigned integers you get by flipping bits in its binary representation (i.e. unset bits must be set, and set bits must be unset).

#this helped http://stackoverflow.com/questions/210629/python-unsigned-32-bit-bitwise-arithmetic

tests = int(input())

for i in xrange(tests):
    num = int(input())
    print ~num & 0xFFFFFFFF

