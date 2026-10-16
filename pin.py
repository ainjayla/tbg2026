# Variant 1
'''
pin = input('Sisesta PIN kood: ')

if pin == '1234':
    print('Õige kood! Sisenesid pangaautomaati.')
else:
    print('Vale kood! Enesehävitusrežiim aktiveeritud ...')
'''

# Variant 2
print('Õige kood! Sisenesid pangaautomaati.'
      if input('Sisesta PIN kood: ') == '1234'
        else 'Vale kood! Enesehävitusrežiim aktiveeritud ...')