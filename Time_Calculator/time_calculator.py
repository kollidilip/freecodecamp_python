def add_time(start, duration, *args):
    
    day_count = 0
    add_hour = 0

    start_hr = int(start.split(" ")[0].split(":")[0])
    startmin = int(start.split(" ")[0].split(":")[1])
    am_pm = start.split(" ")[1]
   
    duration_hours = int(duration.split(":")[0])
    duration_min = int(duration.split(":")[1])
    duration_days = duration_hours // 24
    duration_rem_hrs = duration_hours % 24
    total_duration_mins = duration_hours*60 + duration_min
    # print('duration :', duration)
    # print('duration_days :', duration_days)
    # print('duration_rem_hrs :', duration_rem_hrs)
    # print('duration_min :', duration_min)
    # print('total_duration_mins :', total_duration_mins)
    # add minutes (duration_min) to start minutes
    # print('startmin :', startmin)
    cal_minutes = duration_min + startmin
    # print('cal_minutes :', cal_minutes)

    if cal_minutes >= 60:
        add_hour = cal_minutes // 60
        final_mins = cal_minutes % 60
        # print('add_hour :', add_hour)
    else:
        final_mins = cal_minutes        

    if am_pm == "AM":
        amflag = 1
        if start_hr == 12:
            start_hr = 0
            starthr_changed = 1
    else:
        amflag = 0

    # get final hours
    hours = add_hour + duration_rem_hrs
    if hours == 24:
        adjoc_hour = start_hr
    else:
        adhoc_hour = start_hr + hours
    
    # print("start_hour :", start_hr)
    # print("adhoc_hour :", adhoc_hour)

    final_hour = adhoc_hour % 12
    if final_hour == 0:
        final_hour = 12
    am_pm_cycle =  adhoc_hour // 12
    # print("am_pm_cycle ",am_pm_cycle)
    
    if (am_pm_cycle % 2 == 0):
        finalamflag = amflag
    else:
        finalamflag = not(amflag)

    if finalamflag == 1:
        finalAMPM = "AM"
    else:
        finalAMPM = "PM"


    # print("final_hour :", final_hour)
    # print('final_mins :', final_mins)
    # print("finalAMPM :", finalAMPM)

    if len(str(final_mins)) == 1:
        final_mins = "0"+str(final_mins)
    else:
        final_mins = str(final_mins)    

    if total_duration_mins < 1440:
        if am_pm == "AM" and am_pm_cycle <= 1:
            finaldays = ""
            day_count = 0
        elif am_pm == "PM" and am_pm_cycle > 0:
            finaldays = " (next day)"
            day_count = 1
        else:
            finaldays = ""
            day_count = 0
    elif total_duration_mins >= 1440 and total_duration_mins < 2880:
        if am_pm == "AM":
            finaldays = " (next day)"
            day_count = 1
        else:
            finaldays = " ("+str(duration_days+1)+" days later)"
            day_count = duration_days+1
    else:
        finaldays = " ("+str(duration_days+1)+" days later)"
        day_count = duration_days+1


    if args:
        day_start = args[0].capitalize()
        weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        day_index = weekdays.index(day_start)
        final_day = weekdays[(day_index+day_count)%7]
        # print("start day= :", day_start)
        # print("end day :", final_day)
        # Returns: 12:03 AM, Thursday (2 days later)
        new_time = str(final_hour)+":"+final_mins+" "+finalAMPM+", "+final_day+finaldays

    else:
        new_time = str(final_hour)+":"+final_mins+" "+finalAMPM+finaldays

    
    return new_time
