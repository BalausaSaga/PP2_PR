#1
from datetime import date, timedelta

# Get current date
current_date = date.today()

# Subtract 5 days using timedelta
result_date = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("5 days ago:", result_date)

#2
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# Displaying the results
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
from datetime import datetime

# Get current datetime with microseconds
dt = datetime.now()

# Remove microseconds by replacing them with 0
dt_no_microseconds = dt.replace(microsecond=0)

print("Original:", dt)
print("Without microseconds:", dt_no_microseconds)

#4
from datetime import datetime

# Define two different dates
date1 = datetime(2026, 2, 19, 12, 0, 0)
date2 = datetime(2026, 2, 20, 14, 30, 0)

# Calculate the difference
difference = date2 - date1

# Get total difference in seconds
seconds_diff = difference.total_seconds()

print(f"Difference in seconds: {seconds_diff} seconds")