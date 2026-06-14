
import csv
import pandas as pd

# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
            
# print(temperatures)


df = pd.read_csv('weather_data.csv')
data_dict = df.to_dict()


print(df.temp.mean())
print(df.temp.median())
print(df.to_timestamp.max())