file = open('visits.csv', encoding='UTF-8')

for row in file:
    print(row)

file.close()