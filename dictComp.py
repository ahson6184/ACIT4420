print{number: number * number for number in range(10)}

cities = ["Oslo", "Kathmandu", "Barcelona", "Shanghai", "Seoul"]

#print{ city:" World's best city" for city in cities }

print{ city: [0 for _ in range(7)] for city in cities }
