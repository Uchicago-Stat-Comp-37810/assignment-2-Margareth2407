#!/usr/bin/env python
# coding: utf-8

# In[1]:


cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")


# In[2]:


cars = 100 #setting car equal to 100
space_in_a_car = 4.0 #setting space_in_a_car equal to 4.0
drivers = 30 #setting drivers equal to 30
passengers = 90 #setting passengers equal to 90
cars_not_driven = cars - drivers #calculating cars_not_driven as cars minus drivers
cars_driven = drivers #setting cars_driven equal to drivers
carpool_capacity = cars_driven * space_in_a_car #calculating carpool_capacity as cars multiplies by space_in_cars
average_passengers_per_car = passengers / cars_driven #calculating carpool_capacity as [assenges divided by cars_driven


print("There are", cars, "cars available.") #printing text, calculated number of cars and text
print("There are only", drivers, "drivers available.") #printing text, calculated number of drivers and text
print("There will be", cars_not_driven, "empty cars today.") #printing text, calculated number of cars_not_driven and text
print("We can transport", carpool_capacity, "people today.") #printing text, calculated number of carpool_capacity and text
print("We have", passengers, "to carpool today.") #printing text, calculated number of passengers and text
print("We need to put about", average_passengers_per_car,
      "in each car.") #printing text, calculated number of average_passengers_per_car and text


# In[ ]:




