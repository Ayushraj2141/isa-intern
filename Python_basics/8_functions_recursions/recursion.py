'''
Recursion --> a function calling itself 
function khud ko hi call krega'''

# isko smjhne ka best tareeka hai factorial

def fact(n):
  
    if(n ==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

n = int(input("Enter number whose factorail is to be calculated"))
print(f"The factorial of the number {n} is {fact(n)}")


'''
don't forget to write the base condition 
otherwise the recursion will keep calling itself for infinite number of times 
-- stack overflow'''