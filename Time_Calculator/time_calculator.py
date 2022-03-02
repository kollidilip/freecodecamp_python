def add_time(start, duration, *args):

    st_time = start.split(" ")[0]
    st_hr = int(st_time.split(":")[0].strip())
    st_mm = int(st_time.split(":")[1].strip())
    am_pm = start.split(" ")[1].strip()

    du_hr = int(duration.split(":")[0].strip())
    du_mm = int(duration.split(":")[1].strip())

    # print (st_hr,st_mm,du_hr,du_mm)

    if args:
        new_time = compute_time(st_hr,st_mm,du_hr,du_mm,am_pm,args[0])
    else:
        new_time = compute_time(st_hr,st_mm,du_hr,du_mm,am_pm)

    return new_time

def compute_time(st_hr,st_mm,du_hr,du_mm,am_pm,*args):
    computedtime = ''
    # print(type(st_hr ))
    # print(type(st_mm ))
    # print(type(du_hr ))
    # print(type(du_mm ))
    # print(type(am_pm ))

    mins = st_mm + du_mm
    if mins > 59:
        mins = mins%60
        hrs = mins/60
    elif mins == 60:
        pass
    return computedtime