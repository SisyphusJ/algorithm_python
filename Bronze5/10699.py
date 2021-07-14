import datetime

d = datetime.datetime.now()
print(str(d.year).zfill(4) + "-" + str(d.month).zfill(2) + "-" + str(d.day).zfill(2))
