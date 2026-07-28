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

Loop through the file line by line:

with open("inheritance.py",'r') as f :
   for i in f :
        print(i)