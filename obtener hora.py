from datetime import datetime

date = datetime.now()
print("Before Formatting")
print("DateTime:", date)
print("Date:", date.date())
print("Time:", date.time())
print("After Formatting")
print("DateTime:", date.strftime("%d %B, %Y %H:%M:%S")) # DD Month, YYYY HH:MM:SS
print("Date:", date.date().strftime("%d %B, %Y")) # DD Month, YYYY
print("Time:", date.time().strftime("%H:%M:%S")) # HH:MM:SS