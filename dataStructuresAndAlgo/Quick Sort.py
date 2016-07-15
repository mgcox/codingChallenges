'''Quick Sort is a sorting algorithm that focuses on using a pivot item (first item, medi) and partitions the rest of the
objects around that item. Basically all items are sorted as the items less than the pivot before it and the items greater
go after the pivot'''

#Best Case O(n log(n)) Average O(n log(n)) Worst O(n^2)

'''We will pick the last element for this practice'''



#choose the last item in the array/subarray as the pivot and sort accordingly
def partition(arr,lowIndex,highIndex):

    #set pivot at end of group/array
    pivot = arr[highIndex]

    #Smallest element or location of "wall"
    wall = lowIndex - 1

    #move all elements that are less than (or equal to) the pivot to the other side of "wall"
    for j in range(lowIndex,highIndex):
        if arr[j] <= pivot:
            # move wall over one
            wall += 1
            arr[wall],arr[j] = arr[j],arr[wall]

    #move pivot to its proper spot by swapping it with the wall index + 1
    arr[wall+1], arr[highIndex] = arr[highIndex], arr[wall+1]

    #return the location to the right of the wall
    return wall+1


def quickSort(arr,lowIndex,highIndex):
    if lowIndex < highIndex:

        #partition
        wallLocation = partition(arr,lowIndex,highIndex)

        #sort the left side to wall
        quickSort(arr,lowIndex,wallLocation-1)
        #sort the right side to wall
        quickSort(arr,wallLocation+1,highIndex)


arr = [2,4,10, 7, 8, 9, 1, 5]

n = len(arr)

#The high index is to the left of the last index (n - 1)
quickSort(arr,0,n-1)

#Print out the array in sorted version
for i in range(n):
    print ("%d" %arr[i]),