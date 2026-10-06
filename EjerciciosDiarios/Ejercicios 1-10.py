Hours = input('Enter Hours: \n')

Rate = input('Enter Rate: \n')

try:



    horasextra = Hours - 40

    if Hours> 0 and Hours<=40 :
        calculonormal=Hours*Rate
        print(calculonormal)
    else :
        calculounocinco=40*Rate + (horasextra * (Rate*1.5))
        print(calculounocinco)

except :
    print("Error,please enter numeric input")





