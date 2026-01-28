# CityBikeGo Data Analytics Activity
# Using Sets, Tuples, and Dictionaries

# =========================
# Sample Data
# =========================

customerListMonthOne = [
    "Ali", "Ben", "Ali", "Dana", "Cara", "Ben"
]

customerListMonthTwo = [
    "Ali", "Ella", "Ben", "Frank", "Cara", "Ben"
]

bookingData = [
    ("Ali", "StationA", "Weekday", 2),
    ("Ben", "StationB", "Weekend", 1),
    ("Ali", "StationA", "Weekday", 3),
    ("Cara", "StationC", "Weekday", 2),
    ("Ella", "StationB", "Weekend", 2)
]

loyalCustomers = {"Ali", "Cara"}

# =========================
# SETS – Customer Analysis
# =========================

monthOneSet = set(customerListMonthOne)
monthTwoSet = set(customerListMonthTwo)

uniqueCustomers = monthOneSet.union(monthTwoSet)
regularCustomers = monthOneSet.intersection(monthTwoSet)
newCustomers = monthTwoSet.difference(monthOneSet)
inactiveCustomers = monthOneSet.difference(monthTwoSet)

# =========================
# TUPLES – Booking Records
# =========================

firstBooking = bookingData[0]
customer, station, dayType, duration = firstBooking

# =========================
# DICTIONARIES – Analytics
# =========================

customerHours = {}
stationActivity = {}

for customer, station, dayType, duration in bookingData:
    customerHours[customer] = customerHours.get(customer, 0) + duration
    stationActivity[station] = stationActivity.get(station, 0) + 1

busiestStation = max(stationActivity, key=stationActivity.get)

# Dic
