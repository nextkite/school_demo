from datetime import timedelta
import datetime

temp_num = timedelta(seconds=5)
date_temp = datetime.datetime.now()
print(date_temp)
date_temp = date_temp + temp_num
while True:
    if datetime.datetime.now() > date_temp:
        print("******")
        break









