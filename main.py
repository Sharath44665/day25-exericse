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

# w_data = pandas.read_csv("weather_data.csv")
# # print(w_data)
# # print(w_data["temp"])
#
# w_dict=w_data.to_dict()
# print(w_dict)
# w_list=w_data["temp"].to_list()
# # avg_temp=sum(w_list) / len(w_list)
# # print(avg_temp)
# # _______________________or
# avg_temp=w_data["temp"].mean()
# print(avg_temp)
# max_temp=w_data["temp"].max()
# print(max_temp)

# monday_row = w_data[w_data["day"] == "Monday"]
# print(monday_row)
#
# high_temperature=w_data[w_data["temp"]==w_data["temp"].max()]
# print(high_temperature)

# w_data[w_data["day"]=="Monday"]
# actual_temp=int(monday_row["temp"])
# far_temp=actual_temp *9/5 +32
# print(far_temp)

# create a dataframe from scractch
# data_dict={
#     "students": ["name1","name2","name3",],
#     "score":[95,65,75]
# }
#
# actual_data=pandas.DataFrame(data_dict)
# print(actual_data)
# actual_data.to_csv("student_data.csv")
# download from here:https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
squirrel_data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel=squirrel_data[squirrel_data["Primary Fur Color"]=="Gray"]
grey_squirrel=len(grey_squirrel)
black_color=squirrel_data[squirrel_data["Primary Fur Color"]=="Black"]
black_color=len(black_color)
red = squirrel_data[squirrel_data["Primary Fur Color"]=="Cinnamon"]
red= len(red)

my_data={
    "grey squirrel": [grey_squirrel],
    "black squirrel": [black_color],
    "Red squirrel": [red]
}

my_analytics_data=pandas.DataFrame(my_data)
my_analytics_data.to_csv("my_analytics.csv")
