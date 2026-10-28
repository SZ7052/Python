num1 = 0
num2 = 1
num3 = 0

print(num1, end=",")
print(num2, end=",")

for i in range(8):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    if i < 7: #Simplemente para que el último no tenga "," depués.
        print(num3, end=",")
    else:
        print(num3)