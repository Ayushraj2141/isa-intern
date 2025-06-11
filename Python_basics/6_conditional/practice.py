# # Q-1 to find greatest of numbers 
# # M-1 using arrays 
# how_many = int(input("Values "))
# num = []
# ## Aim is to find the greatest of all input digits 
 
# for i in range(how_many):
#     take = int(input(f"Take value number {i+1} : "))
#     num.append(take)
# print(num)
    
# '''
# why the hell is this not woorking
# my aim was that i will add this in an array 
# then sort the array in descending order 
# and then print the first index of that array this would have given me the required answer 
# '''
# # const = final.sort()
# # print(const[0])
    
    
    
# M-2
# how_many = int(input("Values "))
# for i in range(how_many):
#     take = int(input(f"Take value number {i+1} : "))
#     #naah now this i won't be able to take the values in a loop
#     # check this also one's


# M-3 The teacher's method 
# a = int(input("Enter number 1 : "))
# a1 = int(input("Enter number 2 : "))
# a2 = int(input("Enter number 3 : "))
# a3 = int(input("Enter number 4 : "))
# if(a>a1 and a>a2 and a1>a3):
#     print("Greatest number is 1st ")
# elif(a1>a and a1>a2 and a1>a3):
#     print("Greatest number is 2nd ")
# elif(a2>a and a2>a1 and a2>a3):
#     print("Greatest number is 3rd ")
# else:
#     print("4th number is greatest ")
    
    
    
## in keyboard checks if the string or char is present in the total string
take = input("Enter the string to check ")
if("Ayush".lower() in take.lower()): # ab ye shi kaam hogyaa kyunki hamnee ab jo khel k niyaam hai woh hrr jgh braabar kr diyee hai like ab baati lower case ki hi horhii haii pure text context mai 
# iske baad kuch utpatang jaise AyuSH wgeraa bhi hogaa tb bhi kaam kregaa araam se
    print("True")
else:
    print("false")
    