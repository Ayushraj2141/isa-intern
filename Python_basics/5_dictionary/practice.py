how_much = int(input("Enter how many key value pairs you want to add "))
d = {}
for i in range(how_much):
    keys = input(f"Enter the name of the student {i+1} ")
    for j in range(how_much-1): #check this there is some issue with this loop
        values = int(input(f"Enter how much marks {keys} got "))
    d.update({keys:values})
print(d)
print(d.values())

                     