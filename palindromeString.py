#The most basic version of comparing a palindrome string done in python
palString = str(raw_input())

#Check if the string is the same as its reversed version
print palString == palString[::-1]