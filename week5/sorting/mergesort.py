def mergeSort(nlist):
    print("Splitting", nlist)
    
    # insert your code to complete the mergeSort function
    if len(nlist) > 1:
        #At the merge sort it divids the list in halve into 2 subsets every recursive call
        lefthalf = nlist[:len(nlist) // 2]
        righthalf = nlist[len(nlist) // 2:]
                 
        #Sort the left side of the list first with the recursive call
        mergeSort(lefthalf)
        #Sort the right side of the list second with the recursive call
        mergeSort(righthalf)
        #Merge the final list starting with the right side of the list, so that the values are in order
        merge(nlist, righthalf, lefthalf)
        
    print("Merging ",nlist)   
    

def merge(nlist,lefthalf,righthalf):
# i is a counter for the left, j is a counter for the right, and k is for the merge    
    i=j=k=0       
    # Checking that i is < left and j < the right length in order to know when to stop, dividing the list into further sub-list
    while i < len(lefthalf) and j < len(righthalf):
    # Checking if the first spot in the left side of the list is < the first spot on the right side of the list.    
        if lefthalf[i] < righthalf[j]:
        # Place the value into the lower spot of the sorted list    
            nlist[k]=lefthalf[i]
            i=i+1
        # The right half has the smaller number
        else:
            nlist[k]=righthalf[j]
            j=j+1
        # This moving the counter of the sorted list
        k=k+1
    # Finished sorting the first half and proceeding to sort the second half of the list
    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1
    # This will sort the right side of the list
    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    # Returns the sorted list
    return nlist
# List to be sorted
nlist = [55, 31, 26, 20, 63, 7, 51, 74, 81, 40]
# Sorted list
mergeSort(nlist)
# Final output showing sorted list 
print("Sorted: ",nlist)

# The running time complexity for best case, worst case, and average-case scenario is O(n*log n)

# The space complexity of the algorithm is O(n)

