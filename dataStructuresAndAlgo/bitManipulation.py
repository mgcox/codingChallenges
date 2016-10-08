num = 10

#bit shift over 4
print(num << 1)

print(bin(num))

inverse = ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)

#print(bin(inverse))
#print(num)



print(num - 1)
print(bin(~(num-1)))
#get lowest bit
print(num & ~(num - 1))



