# # code hmaraa save hojayee in file hum ye chahtee hai abhi k liyeee
# ''' 
# program chalaa -- result aayaa 
# fir close krke sb khtm hojayegaa 
# ye resulted data khi save nhi hogaa
# RAM mai save hota hai waisee volatile -- non saving data 
# file mai write krnaa 
# hum krtee ram directly kyun nhi -- kyunki ram kaafi fast hoti hai 
# file type -- 1. text(.txt) and  2. binary file(.dat)'''

# f = open("file.txt","r") # r is read mode as if kis mode mai humme file ko kholnaa hai
# data = f.read()
# print(data)
# f.close() #This closses the open file for further access and avoid any vulnerability

# # pata nhi ye kaam nhi krrhaa hai isse dekhnaa ek baarii


# # Write to a file

# st = "This is so awesome"

# f = open("myfile.txt","w")
# f.write(st)
# f.close() #  ye kaam krgyaa yayy

'''
isme pdhne k liyee bht kuch hai revise krtee hue issee dekhnaa 
kaafi saare functions hai jaha tk mujhe yaad hai
readlines readline pickle wgera krke bhi kuch thaa ek baar dekhnaa
'''

'''
r-- read 
w -- write agr nhi hai bn jayegi and overite 
a -- write aage 
fir r+ , rb wb wgeraa bhi hota hai ye dekhnaa ''' 


# can also use with function to remove f.close() or something like that 
# with open("file.txt", "a+") as f:
#     print(f.read())