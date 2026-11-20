from pprint import pprint

file = open('visits.csv', encoding='UTF-8')

visits = {}
for row in file:
    pair = row.strip('\ufeff').split(';')
    visits[pair[0].strip()] = int(pair[1].strip())
file.close()

max = 0
max_key = ''

for visit in visits:
    if visits[visit] > max:
        max_key = visit
        max = visits[visit]

# pprint(visits)

print('Kõige rohkem külastusi oli ' 
    + max_key
    + ', siis külastas parki '
    + str(visits[max_key])
    + ' inimest')