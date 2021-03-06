#solving problems with python project
#01 - problem
# Source: https://projecteuler.net/problem=2 || Note: you should have account and login to see problems

#  Problem is:
    # Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
    # By starting with 1 and 2, the first 10 terms will be:
    #        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    # By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
    # find the sum of the even-valued terms.
    
def fib(n):
    ''' Take a n as a taregt number, find Even Fibonacci to n number'''
    a,b = 0,1
    fib_list = []
    while a<n:
        if a%2==0:
            fib_list.append(a)
        a, b=b, a+b
    return fib_list
print(sum(fib(4000000)))