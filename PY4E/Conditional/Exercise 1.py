# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly
# rate for hours worked above 40 hours.
#
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

Hours=int(input("Ingrese el numero de horas: "))
Rate=float(input("Ingrese el numero de horas: "))

HorasExtra=Hours-40
RateExtra=Rate*1.5

if Hours > 0 and Hours <= 40:
    Pay = Rate * Hours
else:
    Pay = (Rate * 40 )+(RateExtra * HorasExtra)

print(Pay)