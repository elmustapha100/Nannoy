"""First exercise on the Python Workshop"""
"""Building an Employee Profile Generator"""

first_name = "John"
last_name = "Doe"

full_name = first_name +" "+ last_name
print(full_name)
address = input("Home address : ")
age = int(input("Age : "))

employee_info = full_name + " is " + str(age) + " years old"
years_of_experience = str(input("How many years of work experience do you have ? : "))
experience_info = 'Experience: ' + years_of_experience + ' years'
job_position = input("Enter your job position in the company :  ")
salary = int(input("How much is your salary :  "))
employee_card = f"Employee: {full_name} | Age: {age} | Position: {job_position} | Salary: NGN{salary}"
print(employee_card )