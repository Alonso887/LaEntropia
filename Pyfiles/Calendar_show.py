import os, time, datetime
from datetime import timedelta
date_info = [[],[],[],[],[],[],[]]#Here i save the weeks info to show, the weekdate function retursn values from 0-6 so is very conveniento to use a list
user_input = [None,None]
def calendar_p1():# Just putting these in functions to make it clearer, nothing that complicated
    print("+--------" * 7,end='')
    print("+")
def calendar_p2():
    print("|        "* 7,end='')
    print("|")
def calendar_p3(vals,fd):
     for i in vals:
         dt = fd + timedelta(days=i)
         ds = dt.day
         print(f"|   {ds}   ",end='')
         if len(str(ds)) < 2:
             print(" ",end='')
     print("|")
def print_calendary(final_date):
    print("                            CALENDAR\n  MONDAY  TUESDAY  WEDNESDAY THURSDAY  FRIDAY SATURDAY  SUNDAY")
    calendar_p1()
    calendar_p2()
    calendar_p3([0,1,2,3,4,5,6],final_date)
    calendar_p2()
    calendar_p1()
    calendar_p2()
    calendar_p3([7,8,9,10,11,12,13],final_date)
    calendar_p2()
    calendar_p1()
    calendar_p2()
    calendar_p3([14,15,16,17,18,19,20],final_date)
    calendar_p2()
    calendar_p1()
    calendar_p2()
    calendar_p3([21,22,23,24,25,26,27],final_date)
    calendar_p2()
    calendar_p1()
    calendar_p2()
    calendar_p3([28,29,30,31,32,33,34],final_date)
    calendar_p2()
    calendar_p1()
    calendar_p2()
    calendar_p3([35,36,37,38,39,40,41],final_date)
    calendar_p2()
    calendar_p1()

def input_interpretation(p):#just making sure the date_info variable gets the right values
    selected_date = datetime.datetime(p[0],p[1],1)
    while True:# 0 is Monday so i just take 1 from the date until is monday so the calendar looks good
        final_date = datetime.date.weekday(selected_date)
        if final_date != 0:
            final_date = datetime.date.weekday(selected_date)
            selected_date = selected_date - timedelta(days=1)
        else:
            break
        selected_date = selected_date - timedelta(days=1)
        return selected_date
    

print("============")
print("CALENDAR.PY")
print("============")
print("\nHi, insert a year and a month to see the calendar of that date (plase use only numbers) ")
user_input[0] = int(input("Year: "))
user_input[1] = int(input("Month: "))
print_calendary(input_interpretation(user_input))
