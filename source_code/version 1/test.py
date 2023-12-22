
from datetime import datetime

# Get current date and time
current_datetime = datetime.now()

# Format the current date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print("Current Date and Time:", formatted_datetime)

# If you want to get only the current date
current_date = current_datetime.date()
formatted_date = current_date.strftime("%Y-%m-%d")

print("Current Date:", formatted_date)