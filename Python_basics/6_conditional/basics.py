# if -- else -- elif 
# agr koi condition tab ye wo etc krengeee 
age = int(input("Enter your age "))
if(age>=18) :
    print("Eligible for voting") # agar ye true hoga toh else execute hi nhi hogaa

    
# elif agar do se zyada conditions ko check krna hai tb use krnege 

elif(age<0 or age >150):
    print("You are entering wrong number ") 
else:
    print("not valid for voting")

## ye note dene wali baat hai ki control flow mai saari ki saari conditions check nhi hoti hai
## Agar sirf ek hi if hoo uske saath koi else ya elif nahi hogaa toh woh independently kaam kregaa uskoo kisi saath k zroorat nhii haii
## also sirf else or sirf elif kaam nhi kregaa 