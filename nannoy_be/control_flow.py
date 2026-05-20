#control flow statement in Python 
# status_code = 404 

# if status_code == 200:
#     print("OK — request succeeded")
# elif status_code == 400:
#     print("Bad Request — client sent invalid data")
# elif status_code == 401:
#     print("Unauthorized — authentication required")
# elif status_code == 404:
#     print("Not Found — resource does not exist")
# elif status_code >= 500:
#     print("Server Error — something went wrong on our end")
    
# else:
#     print(f"Unhandled status code: {status_code}")


# for i in range(3): 
#     if i == 1 : 
#         continue    #the "continue" statement skips to the next iteration of the loop.
        
#     print(i)

user_record = ['username','email','password']
payload = {'username':'Jacobi',
'email':',
'password':'secret'}

missing = []

for user in user_record : 
    if not payload.get(user): 
        missing.append(user)