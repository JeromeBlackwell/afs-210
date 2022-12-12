
# def loop1():
#     # Sum the odd numbers between 1 and 20
#     odd_sum = 0
#     for i in range(20):
#         if (i % 2) == 1:
#             odd_sum += i
#     return odd_sum

# def loop2():
#     # Sum the even numbers between 1 and 20
#     i = 0
#     even_sum = 0
#     while i < 20:
#         if (i % 2) == 0:
#             even_sum += i
#         i += 1
#     return even_sum

# def loop1Rec(num,odd_sum):
    # Duplicate the loop1 function using recursion

# def odd_sum(num1,num2):
#     if (num1>num2):
#         return 0
#     return num1 +odd_sum(num1+2,num2)
# num1=1
# print("Enter Odd Number")
# num2=int(input())
# print("Sum of off numbers between 1 and 20:",odd_sum(num1,num2))

# def loop2Rec(num,even_sum):
#     # Duplicate the loop2 function using recursion

def even_sum(x,y):
    if (x>y):
        return 0
    return x +even_sum(x+2,y)
x=2
print("Enter Even Number")
y=int(input())
print("Sum of odd numbers between 1 and 20:",even_sum(x,y))