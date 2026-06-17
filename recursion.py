# PRINT NUMBERS FROM 1 TO N

# Using loop
# n = 5
# i = 1
# while i <= n:
#     print(i, end=" ")
#     i += 1


# using recursion
def printNumbers(i, n):
    # base case
    if i > n:
        return
    # recursive case
    print(i, end=" ")
    # uske baad i ki value ko badhana h and same chiz fir se karni h
    printNumbers(i+1, n)


# FACTORIAL KA CODE BHI AISE HI KARNA H
def factorial(n):
    if n == 0:
        return 1
    return n*(n-1)


print(factorial(7))


# recursive stack
def fun(n):
    if n == 0:
        return
    fun(n-1)
    print(n, end=" ")


print(fun(3))


# RECURSIVE TREE [LEETCODE =(509)]
