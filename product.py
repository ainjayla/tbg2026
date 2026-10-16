name = input('Sisesta toote nimi: ').lower()

product = ''
price = 0.0

if name == 'maasikas':
    product = name
    price = 5
elif name == 'vaarikas':
    product = name
    price = 5.2

print(product.capitalize() + ' maksab ' + str(price) + ' eurot'
      if product != ''
        else 'Meil ei ole sellist toodet')