Hours=int(input('Enter Hours: \n'))

Rate=int(input('Enter Rate: \n'))

horasextra=Hours-40


if Hours> 0 and Hours<=40 :
    calculonormal=Hours*Rate
    print(calculonormal)
else :
    calculounocinco=40*Rate + (horasextra * (Rate*1.5))
    print(calculounocinco)





