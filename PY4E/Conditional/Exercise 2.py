# Exercise 2: Rewrite your pay program using try and except
# so that your program
# handles non-numeric input gracefully
# by printing a message and exiting the program.
# The following shows two executions of the program:
#
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

try:
    Hours=int(input("Ingrese el numero de horas: "))
    Rate=float(input("Ingrese el numero de horas: "))
    HorasExtra = Hours - 40
    RateExtra = Rate * 1.5
    if Hours > 0 and Hours <= 40:
        Pay = Rate * Hours
    else:
        Pay = (Rate * 40) + (RateExtra * HorasExtra)
        print(Pay)
except ValueError:
    print("Error, please enter numeric input")





