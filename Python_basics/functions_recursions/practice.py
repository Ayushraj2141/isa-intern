# # function to find sum of first n natural numbers

# def sum(n):
#     if(n == 1) :
#         return 1
#     else:
#         return (n+sum(n-1)) ## yahaa + nhi - hi aayega ye dhyaan rkhnaa yee wali gltii nhi krni haii yaad seee
    
# n = int(input("Enter till where you want to find the sum "))
# print(f"sum of first {n} number is {sum(n)}")

# there is a round function which rounds off the number to given (f"{round(c,2)}")

## return statement matlab baat khtm ab ye cheeze uskee aage nhi chlegaa ye last line hai function mai jo code editor read kregaa 


# Q-2 star patter using recursion
def pattern(n):
    if(n==0):
        return
    print(" * " * n )
    pattern(n-1)
    
pattern(3)
        