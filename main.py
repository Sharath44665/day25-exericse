# with open("weather_data.csv") as myfile:
#     w_data=myfile.readlines()
#     print(w_data)

import csv

# with open("weather_data.csv") as myfile:
#     w_data=csv.reader(myfile)
#     # print(w_data)
#     temperature_data=[]
#     count=0
#     for row in w_data:
#         if count != 0:
#             temp=row[1]
#             temperature_data.append(int(temp))
#         count+=1
#
#     print(temperature_data)

import pandas
w_data= pandas.read_csv("weather_data.csv")
print(w_data)
print(w_data["temp"])