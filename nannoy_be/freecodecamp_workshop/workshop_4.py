"""For this workshop , using conditional statements to determine 
whether commuting is possible based on the weather,the distance to 
travel,and the availability of a vehicle.

objective: Fulfill the user stories below and get all the tests to pass to complete
the workshop exercise .

User stories: 
1. Create the following variables : 
  -distance_mi (a number representing the distance to travel in miles)
  -is_raining(a boolean representing if the user is currently experiencing rainy weather)
  -has_bike(a boolean representing if the user has a bicycle)
  -has_car(a boolean representing if the user has a car)
  -has_ride_share_app(a boolean representing if the user has an app that allows them  to request a ride)

2.Using conditional statements to determine whether commuting is possible based on the values of the variables
3.Using "if, elif and else" statements to evaluate the distance categories in ascending order.
4. if distance_mi is a falsy value :
     print False 

5.If the distance is less than or equal to a mile : 
    . print True only if its raining 
    . otherwise , print false 

6.If the distance is greater than a mile and less than or equal to 6miles: 
    . print True only if the person has a bike and it's not raining 
    . otherwise ,print false 

7. if the distance is greater  than 6 miles :
    . print True if the person has a car or has a ride_share_app.
    . otherwise ,you should print False               
"""

distance_mi = int(input("How many miles is your journey : "))
is_raining = True 
has_bike = True
has_car = True 
has_ride_share_app = False

distance_mi = int(input("How many miles is your journey : "))
is_raining = True 
has_bike = True
has_car = True 
has_ride_share_app = False

if distance_mi == 0 : 
    print(False)
elif distance_mi <= 1 and is_raining: 
    print(True)
elif distance_mi >= 1 and distance_mi <= 6 :
    if has_bike and not is_raining :
        print(True)
elif distance_mi > 6 :
    if has_car or has_ride_share_app :
        print(True)         
else : 
    print(False)        
