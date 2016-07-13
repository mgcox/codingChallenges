'''Given a number having only one ‘1’ and all other ’0’s in its binary representation, find position of the only set bit.
 If there is only one '1' bit then print that position else print -1.
Position of  set bit '1' should be counted starting with 1 from LSB side in binary representation of the number.'''


t = int(raw_input())

for i in range(0,t):
    num = bin(raw_input())
    s