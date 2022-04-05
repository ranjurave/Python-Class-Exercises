cities = []
infile = open('cities.txt', 'r')
citiesFile = infile.readlines()
print(citiesFile)
infile.close()
for city in citiesFile:
    cities.append(city.strip('\n'))
for city in cities:
    print (city)
