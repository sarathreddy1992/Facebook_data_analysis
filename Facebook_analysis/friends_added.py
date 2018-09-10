import timestring
import json
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta
import tabulate
import dateutil.parser


def friends_added(file_path):
    file_path = file_path+'/friends.json'
    if not file_path:
        print("Failed to open the specified path")

    #reading all the json files

    with open(file_path , 'r') as f:
        frnd = f.read()

    # load json data
    friends_data = json.loads(frnd)
    # print(friends_data)
    dates = []
    for i in friends_data["friends"]:
        dates.append(timestring.Date(i["timestamp"]))

    # print(dates)


    date_time_format = []
    # converting the data into readable dates
    for i in range (0,len(dates),1):
        date_time_format.append(dates[i].date)

    # print(date_time_format)


    firstdate, last_date = date_time_format[-1], date_time_format[0]

    print("The first date to add a friend on facebook" ,firstdate,"and the last date to add a friend ",last_date)

    num_of_days = last_date - firstdate
    # print(num_of_days)

    total_sec = num_of_days.total_seconds()
    # print(total_sec)
    num_of_days = int(total_sec/86400) +1
    # print(num_of_days)

    # num_of_days = int(num_of_days.total_seconds()/86400)+1
    print("The number of days active on facebook is ",num_of_days)

    #creating arrays to count the number of friends added on each day and each month


    friends_added_on_a_day = [0] * int(num_of_days)
    friends_added_in_a_month = [0] *13


    # # count number of friends each day, cumulative
    for i in range(len(date_time_format)):
         days_diff = (date_time_format[i] - firstdate).total_seconds() / 86400
         friends_added_on_a_day[int(days_diff)] += 1
         friends_added_in_a_month[date_time_format[i].month] += 1

    xaxis =[]

    for i in range(num_of_days):
        xaxis.append(datetime.now() - timedelta(days=num_of_days - i))

    total_friends = np.cumsum(friends_added_on_a_day).tolist()



    # plotting graphs in accordance with friends added in each day
    fig, ax = plt.subplots()
    ax2 = ax.twinx()
    ax.plot(xaxis, friends_added_on_a_day, color='C2', label='number of friends added ')
    ax.set_ylabel('Friend added each day')


    ax2.plot(xaxis, total_friends, color='C5', label='Friends so far')
    ax2.set_ylabel('Friends so far')
    plt.legend(loc='upper left', ncol=2)
    plt.show()

    plt.plot(range(13), friends_added_in_a_month, label='per month')
    plt.legend(loc='upper left', ncol=2)
    plt.show()


friends_added('friends')
