def binary_search(list, item):
    list_size = len(list)
    for i in range(list_size):
        if item == list[i]:
            return True
        elif list[i] > item:
            return False
        
list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
list2 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
list3 = ["Alpha", "Beta", "Delta","Epsilon", "Gamma", "Theta", "Zeta"]

print(binary_search(list,31))
print(binary_search(list,77))
print(binary_search(list3, "Delta"))
