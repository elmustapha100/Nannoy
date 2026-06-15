#dictionaries : a built-in data structure that stores data 
#in a key-value pair , ordered ,mutable collection but do not allow duplicates .

# user_data = {
#     'name' : "Jack Bauer",
#     'id' : 12356,
#     'category' : "First class citizen",
# }

# print(user_data['id'])
# print(user_data.get('category'))

# for user in user_data.items():
#     print(user) 

products = {
    'Laptop' : 10000,
    'Iphone 17': 15000,
    'headphone': 2000,
}

for product ,price in products.items(): 
    products[product] = round(price * 0.7) #a discount of 30%.
print(products)