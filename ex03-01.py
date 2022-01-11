hour = input ("How many hours work this week? ")
rate = input ("Which rate will pay per hour? ")
frate =float(rate)
fhour=float(hour)
if fhour > 40:
    pay = (40*frate)+((fhour-40)*(frate*1.5))
else:
        pay = frate * fhour
print("Amount to pay is:", pay)
