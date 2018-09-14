#solving problems with python project
#01 - problem
# Source: https://projecteuler.net/problem=1 || Note: you should have account and login to see problems

#  Problem is:
    #If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    #Find the sum of all the multiples of 3 or 5 below 1000.
# First sovle: function way 
def mltuiple3or5():
    sums = []
    for n in range(1, 1000):
        if n % 3 == 0 or n % 5 == 0 :
            sums.append(n)
    #print(sums) # for printinh all elements 
    return sum(sums)
#print(mltuiple3or5())

# Second solve: comperasion way
mul3or5 = sum([n for n in range(1,1000) if n%3==0 or n%5==0])
print(mul3or5)