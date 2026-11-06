# Variant 1
length = float(input('Sisesta oma pikkus (cm): '))
weight = float(input('Sisesta oma kaal (kg): '))

bmi = round(weight / (length / 100) ** 2, 1)
print('Sinu kehamassiindeks on ' + str(bmi))

if bmi < 16:
    print('Tervisele ohtlik alakaal')
elif 16 <= bmi < 19:
    print('Alakaal')
elif 19 <= bmi < 25:
    print('Normaalkaal')
elif 25 <= bmi < 30:
    print('Ülekaal')
elif 30 <= bmi < 35:
    print('Rasvumine')
elif 35 <= bmi < 40:
    print('Tugev rasvumine')
elif 40 <= bmi:
    print('Tervisele ohtlik rasvumine')

# Variant 2
'''
print('Sinu kehamassiindeks on ' +
      str(round(float(input('Sisesta oma kaal (kg): ')) /
                (float(input('Sisesta oma pikkus (cm): ')) / 100) ** 2, 1)))
'''