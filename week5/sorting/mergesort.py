def mergeSort(nlist):
    print("Splitting", nlist)
        # insert your code to complete the mergeSort function
    
    if len(nlist) > 1:
        
        lefthalf = nlist[:len(nlist) // 2]
        righthalf = nlist[len(nlist) // 2:]
        merge(nlist, lefthalf, righthalf)
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(nlist, righthalf, lefthalf)
        
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
mergeSort(nlist) 
print("Sort: ",nlist)



