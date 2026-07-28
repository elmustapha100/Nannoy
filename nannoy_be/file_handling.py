#In python, opening a file goes like this 

f = open("variable.py","r")
print(f.read()) #it opens and reads the entire file 

#opening a file using the with statement 

with open("abstraction_oop.py","r") as f :
    print(f.read())
    f.close() #closing a file


#Read Line method , it returns the first line of the file 
print(f.readline())
print(f.readline())
print(f.readline())

#Loop through the file line by line:

with open("inheritance.py",'r') as f :
   for i in f :
        print(i)

# writing to a file

with open("text.txt",'a') as t :
    t.write("In history of the biggest prize in Mathematics , there are only 3 female mathematicians that got the fields medal.")

# #opening the file after appending 
 with open("text.txt",'r') as t :
    print(t.read())

#overwriting the content of file
with open('text.txt','w') as t :
    t.write("Oooops! File content deleted!")

# # with open("text.txt") as t :
# #     print(t.read())  

#creating a new file
 new_file = open("Newfile.txt","x")          
