hour = input ("How many hours work this week? ")
rate = input ("Which rate will pay per hour? ")
try:
    frate =float(rate)
    fhour=float(hour)
except:
    print("Error, please enter numeric input")
    quit()
if fhour > 40:
    pay = (40*frate)+((fhour-40)*(frate*1.5))
else:
        pay = frate * fhour
print("Amount to pay is:", pay)
