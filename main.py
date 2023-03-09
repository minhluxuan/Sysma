from datetime import datetime, time,timedelta
import pymongo
from detect_person_4 import CountPeople
from sycal import*
import numpy as np
import sycal 

client = pymongo.MongoClient("mongodb://localhost:27017")
interest_level = client["interest_level"]
week_range = interest_level["week_range"]

ID_week_range = int(0)

while True:
    day_range = interest_level["day_range"]
    temp = int(0)
    ID_day_range = int(0)
    maximum = int(0)
    max_time = datetime(2023, 1, 1)
    day_sum_people = int (0)

    while True:

        today = datetime.now()
        den_ta_t = int(0)
        people = int(CountPeople())
        dict_day_range = []

        if people != temp:
            temp = people
            dict_day_range = {"_id":"%d" %ID_day_range,"number_people":"%d" %temp,"time":today.strftime("%H:%M:%S")}
            if people >= maximum:
                maximum = people
                max_time = today
            ID_day_range += 1
            day_range.insert_one(dict_day_range)
            if today.hour == 22:
                break

    time_arr = np.array([])
    people_arr = np.array([])
    query = {"time":1,"number_people":1}
    for data in day_range.find({},query):
        time_arr = np.append(time_arr,str(data['time']))
        people_arr = np.append(people_arr,int(data['number_people']))

    time_arr = sycal.min_convert(time_arr)
    average = sycal.reaverage(people_arr,time_arr)
    
    day_range.insert_one("so nguoi dong nhat ngay %d vao thoi gian" %maximum , max_time)

    dict_week_range = {"_id":"%d" %ID_week_range, "Day":today, "Average":"%f" %average}
    week_range.insert_many(dict_week_range)
    ID_week_range += 1

