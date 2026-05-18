name = input("Enter your name: ")
age = input("Enter your age :  ")
department = input("Enter your department : ")
cgpa =float( input("Enter your CGPA :   "))
is_active = True


total_credit = 20 * 2
first_class = cgpa >= 4.50
award_eligibilty = is_active and (first_class)

print(f"Student: {name}, Age: {age}, Department: {department}, CGPA: {cgpa}, Total Credit: {total_credit}")