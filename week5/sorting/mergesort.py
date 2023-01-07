def mergeSort(nlist):
    print("Splitting ",nlist)
    # insert your code to complete the mergeSort function
    
    if len(nlist) >1:
        mid = len(nlist) // 2
        left = nlist[:mid]
        right = nlist[mid:]
    
    #Recursive call on each half
        mergeSort(left)
        mergeSort(right)
    
    #Two iterators traversing the halvew
        i = 0
        j = 0
    
    #iterator main list
        K = 0
    
    
    print("Merging ",nlist)

def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist

nlist = [55, 31, 26, 20, 63, 7, 51, 74, 81, 40]
