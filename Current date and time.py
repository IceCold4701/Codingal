from datetime import date , time , datetime
#calling the today
#function of data class
today=date.today()
now=datetime.now()
print("Today's day is", today)
print("\nCurrent Date and Time is", now)
#printing date's components
print("\nDate Components", today.year, today.month, today.day)
