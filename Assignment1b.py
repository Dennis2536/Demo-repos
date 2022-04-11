print ("List of months :Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec")
month_name = input("Enter name of month: ")
if month_name == "Mar":
   print ("March is the current month!")
  
elif month_name in ("Apr","Jun","Sep","Nov"):
   print ("No. of days: 30 days")

elif month_name in ("Jan","May","Jul","Aug","Oct","Dec"):
   print ("No. of days: 31 days")

elif month_name in ("Feb"):
   print ("No. of days: 28/29 days") 

else:
   print ("Wrong month name")
   