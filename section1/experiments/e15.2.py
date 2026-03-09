import csv

with open("weather.csv", "r") as file:
    data = list(csv.reader(file))

# print(data)

city = input("Enter a city: ")

for val in data[1:]:
    # print(val)
    if val[0] == city:
        print(val[1])