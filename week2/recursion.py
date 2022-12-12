
def loop1():
#     # Sum the odd numbers between 1 and 20
    i = 0
    odd_sum = 0
    while i < 9:
        if (i % 2) == 0:
            odd_sum += i
        i += 1
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 8:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

# def loop1Rec(num,odd_sum):
#     Duplicate the loop1 function using recursion

def odd_sum(a,b):
    if (a==b):
        return 0
    elif (a % 1==0):
        return a + odd_sum(a+1,b)
    else: return odd_sum(a+1,b)
a=1
print("Enter odd Number")
b=int(input())
print("Sum of odd numbers between 1 and 20:",odd_sum(a,b))
print(loop1())

# def loop2Rec(num,even_sum):
    # Duplicate the loop2 function using recursion
def even_sum(x,y):
    if (x==y):
        return 0
    elif (x % 2==0):
        return x + even_sum(x+1,y)
    else: return even_sum(x+1,y)
x=1
print("Enter Even Number")
y=int(input())
print("Sum of even numbers between 1 and 20:",even_sum(x,y))
print(loop2())