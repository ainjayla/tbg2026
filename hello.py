import sys

name = sys.argv[1]
city = sys.argv[2]

print('Hello', name, 'from', city)
print('Hello ' + name + " from " + city)

# Kuvab ekraanile kõik käsurea argumendid
print(sys.argv)

# Variant 1
print('Mis Su nimi on: ')
name = input()
print('Tere', name)

# Variant 2
name = input('Mis Su nimi on: ')
print('Tere', name)