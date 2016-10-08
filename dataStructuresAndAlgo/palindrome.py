string = "baa"
start = 0
end = len(string) - 1


#we know that the string makes a palindrome without a single character... got until we find that character
while ( start < end and string[start] == string[end]):
    start, end = start + 1, end - 1

print(string[start])
print(string[end -1])
print(start)
print(end)
if (start >= end):
    #we found the spot instantly... aka its a palindrome
    print( -1)
elif ( string[start+1] == string[end] ):
    #the extra char is on the end of the string we found
    stringWithCharacterRemoved = string[:start] + string[start+1:]
    print(stringWithCharacterRemoved)
    if stringWithCharacterRemoved == stringWithCharacterRemoved[::-1]:
        print start
    else:
        print end
else:
    print (end)