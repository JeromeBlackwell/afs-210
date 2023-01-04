def binary_search(list, item):
    low = 0
    high = len(list) -1
    while high >= low:
        mid = (high + low) // 2
        if list[mid] == item:
            return True
        elif list[mid] < item:
            low = mid + 1
        else: 
            high = mid -1   
    else:
        return False
            
list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
list2 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
list3 = ["Alpha", "Beta", "Delta","Epsilon", "Gamma", "Theta", "Zeta"]


print(binary_search(list,31))
print(binary_search(list,77))
print(binary_search(list3, "Delta"))
