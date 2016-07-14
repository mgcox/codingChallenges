#Problem found at http://www.practice.geeksforgeeks.org/problem-page.php?pid=1053

'''Bubble sort is a simple sort that iterates through each value and swaping it with the next
if it is bigger. This is far from the most efficient form of sorting
'''

def bubbleSort():

    #Get the length of the object

    stats = map(int,raw_input().split())
    minutes = stats[0]
    secondsPerSwap = stats[1]
    length = stats[2]

    #Map array
    arr = map(int,raw_input().split())

    swapsNeeded = 0

    for i in range(length):

        '''loop through each value, but stop checking the last elements because they are already in place
        The loop cuts one short so that we can check with the subsequent item in the if statement
        '''
        for j in range(length - i - 1):
            '''Check if the element is bigger than the next, if so
            swap them'''
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapsNeeded += 1


    #We calculate the possible amount of swaps that can be made with the swaps needed
    possibleSwaps = int((minutes*60)/secondsPerSwap)
    if swapsNeeded > possibleSwaps:
        print 0
    else:
        print 1

t = int(raw_input())

for i in range(0,t):

    bubbleSort()
