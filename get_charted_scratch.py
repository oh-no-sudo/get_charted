import datetime 

var = '{dt.year}/{dt.month} {dt.day}'.format(dt=datetime.date(2020, 1, 1))

print(var)

strftime_control = "%A, %d %B %Y"
title="Saturday, 9 May 2020 at 17:30"

control_string = "{dt:%A}, {dt.day} {dt:%B} {dt.year}"

ct_test = control_string.format(dt=datetime.date(2020, 12, 25))
print(ct_test)