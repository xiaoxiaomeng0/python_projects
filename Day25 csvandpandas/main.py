with open("weather_data.csv") as data:
    all_data = data.readlines()
all_data = all_data[1:]
new_all_data = []
for dt in all_data:
    dt = dt.strip("\n")
    new_all_data.append(dt)
print(new_all_data)
