# Q-1 Take names of fruits from the user and add them to the list
# how_many = int(input("Enter how many fruits you want to enter "))
# fruits = []
# for i in range(how_many):
#     take = input(f"Enter the fruit {i+1} : ")
#     fruits.append(take)
# print(fruits)


# Q-2 Take the marks of 6 student and sort them in ascending order 
# how_many = int(input("Enter the total number of students whose marks is to be added "))
# marks = []
# for i in range(how_many):
#     take = int(input(f"Enter the marks of {i + 1 } student : "))
#     marks.append(take)
# print("Unsorted list is " , marks)
# another_marks = marks # Check this why the hell is this coming none 
# print("Sorted list is ", another_marks.sort())

# Q-3 To find the average of marks in a list 
how_many = int(input("Enter the total number of students whose marks is to be added "))
marks = []
sum = 0 
for i in range(how_many):
    take = int(input(f"Enter the marks of {i + 1 } student : "))
    marks.append(take)
list_marks = marks 
print(list_marks)
for i in (list_marks):
    sum = sum + list_marks[i]
    i = i + 1  ## Here i forgot how to access the elements in the list 
print("Average is given by " , sum/how_many)
