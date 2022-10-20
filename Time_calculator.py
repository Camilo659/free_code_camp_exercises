def time_calculator(initial_time, hours, day):
    laps = 0
    days = ['monday', 'tuesday', 'wednesday', 'thursday','friday','saturday','sunday']
    day_in_days = days.index(day.lower())
    push = False
    result = list()

    #Recognizing AM or PM
    try:
        am_pm = initial_time.split()
        am_pm = am_pm[1]
    except:am_pm = False

    try:
        if am_pm == 'AM':began = 'morning'
        elif am_pm == 'PM':began ='late'
    except:pass

    
    try:
        initial_time = initial_time.replace('AM', '')
        initial_time = initial_time.replace('PM', '')
    except:pass

    initial_time = initial_time.replace(':', ' ')
    hours = hours.replace(':', ' ')

    initial_time = initial_time.split()
    hours = hours.split()

    initial_time = [int(x) for x in initial_time]
    hours = [int(x) for x in hours]

    #adding hrs and mins
    for i in range(len(initial_time)):
        result.append(initial_time[i] + hours[i])

    if result[1] >= 60:
        result[0] += 1
        result[1] = result[1] - 60
        push = True

    if began == 'late' and result[0] >= 12:
        laps += 1
    


    while result[0] > 12:
        result[0] = result[0] - 12
            
        if am_pm == 'AM':   am_pm = 'PM'

        elif am_pm == 'PM': am_pm = 'AM'
            
        elif am_pm == False:break

        laps += 1

    if result[0] == 12 and push == True:
        if am_pm == 'AM':   am_pm = 'PM'
        elif am_pm == 'PM': am_pm = 'AM'
        laps += 1

    #Setting the name of the day
    if began == 'morning' and laps < 12:    day = days[day_in_days + int(laps / 2)]

    if began == 'morning' and laps > 12:
        lap_cut = laps
        while lap_cut > 12:
            lap_cut -= 12
        day = days[day_in_days + int(lap_cut / 2) -1]
        
    if began == 'late':
        if 12 > laps >= 1:  day = days[day_in_days + int(laps / 2)]

        if laps > 12:
            lap_cut = laps
            while lap_cut > 12:
                lap_cut = laps - 12
            day = days[day_in_days + int(lap_cut / 2)]
            

    result = [str(x) for x in result]
    if len(result[0]) == 1:result[0] = '0' + result[0]
    if len(result[1]) == 1:result[1] = '0' + result[1]
    print(':'.join(result), am_pm, day, end = ' ')

        
    if laps == 2:print('(Next day)')
    elif laps >= 4 and laps % 2 == 0:print('(', round((laps / 2)), 'days later )')
    elif laps > 2 and laps % 2 != 0:print('(', round((laps / 2) + 0.1), 'days later )')



    if am_pm == False:
        print('The initial time must have AM or PM')

time_calculator('12:00 PM', '50:00', 'monday')









    
    










    







