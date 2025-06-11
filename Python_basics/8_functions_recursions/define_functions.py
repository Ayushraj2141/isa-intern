# a , b ,c = 10,20,30
# print("avg",(a+b+c)/3)

#  this is ok but not so good , this could'nt be reused further 

#  naming a piece of code -- as logic is functions only 

# def avg(): # --> defining a function 
#     take = int(input("Enter how many values you need to input "))
#     sum = 0;
#     for i in range(take):
#         take_value = int(input(f"Enter the value number {i+1} : "))
#         sum = sum+take_value
#     print("Average is " , sum/take) # -- use // to get a integer and avoid floating point number 
    
# avg() # calling a function 

'''
bult in function -- jo already hai jaise print raange len etc
user-defined function -- jo user define krte hai 
kuch built-in function hote hai jo humme import krne hote hai jaise astropy , numpy etc etc..
 
 
 def function(parameter1,parameter2 ) -- function with argument
jaise jaise call kiya jayegaa waise waise aajayegaa 
'''
# def greet(Name,ending):
#     name = input("Enter your name ")
#     print("Hi" , name )
#     print(ending)
    
# greet("Ayush",'thankyou') ## See this how can i give here the name 
# ## like i want ki jab mai apna name loon toh ye woh lele vrna ye fir khud se hi enter your name puchee


# def greet(Name,ending):
#     name = input("Enter your name ")
#     print("Hi" , name )
#     print(ending)
#     return "done" # agar ye nhi krtee toh variable a mai kuch aata nhi actual maii , ye krne se humme function ki value retuen mil gyi hai basically

# # greet("Name","Thanks")
# a = greet("Name","Thanks") # ye none aata agr return na kiya hotaa 
# print(a)

# default paramater(  , ending = " default_value")
# agar koi value nhi diya hogaa toh by default ye milegaa
