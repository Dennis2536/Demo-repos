#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# For your first assignment, create a Python file that will prompt the user to enter a month (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, or Dec); 
# 
# if the user enters one of these, tell the user how many days are in that month. 
# If the user enters March, tell the user, "March is the current month!"
# 
# Stretch goal: allow the user to enter the month number (1-12) OR the month name.

# In[4]:


#Allows user to input the name of a month
month_name = input("Input a month(Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, or Dec): ")


if month_name in ("Feb"): #If month entered by user is February, print the statement below 
	print("No. of days: 28/29 days")
elif month_name in ("Apr","Jun","Sep","Nov"): #If month entered by user is found in this line, print the statement below 
    print("No. of days: 30 days")
elif month_name in ("Jan","May","Jul","Aug","Oct","Dec"):#If month entered by user is found in this line, print the statement below 
    print("No. of days: 31 day")
elif month_name in ("Mar",):#If month entered by user is found in this line, print the statement below 
    print("March is the current month and it has 31days")
else: #Print the statement below when user types an incorrect month name
	print("Wrong month name")


# # # Stretch Goal

# In[5]:


#List all the months and their correspondent number
print("List of months: Jan = 1, Feb = 2, Mar = 3, Apr = 4, May = 5, Jun = 6, Jul = 7, Aug = 8, Sep = 9, Oct = 10, Nov = 11, Dec = 12")

#Allows user to input the name of a month or the month number
month_name = input("Input a month or month number: ")


if month_name in ("Feb",'2'): #If month and number entered by user is found in this line print the statement below 
	print("No. of days: 28/29 days")
elif month_name in ("Apr","Jun","Sep","Nov",'4','6','9','11'): #If month and number entered by user is found in this line print the statement below 
    print("No. of days: 30 days")
elif month_name in ("Jan","May","Jul","Aug","Oct","Dec",'1','5','7','8','12'):#If month and number entered by user is found in this line print the statement below 
    print("No. of days: 31 day")
elif month_name in ("Mar",'3'):#If month and number entered by user is found in this line print the statement below 
    print("March is the current month and it has 31days")
else: #Print the statement below when user types an incorrect number or month name
	print("Wrong month name or wrong number")


# In[ ]:





# In[ ]:




