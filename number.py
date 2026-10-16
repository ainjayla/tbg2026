number = input('Sisesta üks täisarv: ')

if number.isdigit():
    number = int(number)
    result = number + number + 1
    result = result + 9
    result = result / 2
    result = result - number
    print(round(result))
else:
    print('Ära lollita, sisesta normaalne number!')