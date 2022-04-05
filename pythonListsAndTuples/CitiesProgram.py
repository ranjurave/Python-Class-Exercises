cities = ['Auckland','New York','Tokyo','Sydney']
outfile = open('cities.txt','w')
for city in cities:
    outfile.write(city + '\n')
outfile.close()