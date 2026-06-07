# user_id = "EL MUSTAPHA"
# user_id_list = list(user_id) #The list constructor that converts an iterable string into a list.
# print(user_id_list)
# user_id_list = user_id.split(" ") #the splitfuncton
# print(user_id_list)
# del user_id_list[0]# remove an element from a list 
# print(user_id_list)

# #common list methods
# primes = [2,3,5,7,11,13]
# even_number = [2,4,6,8,10]
# primes.extend(even_number)
# print(primes)
# # primes.append(even_number)
# print(primes)
# primes.insert(1,1000)
# print(primes)
# primes.pop(6) #remove an element from a specific index
# print(primes)
# primes.sort()
# print(primes)
# primes.reverse()
# print(primes)


#Tuples : ordered sequence of elements , they are immutable as in constranct to lists
user_id = ("EL Mustapha","Jessica","Gabriel")
for user in user_id :
    if user == "EL Mustapha" :
        continue
    print(user)