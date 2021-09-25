def format_minutes(time):
    time_hours = int(time/60)
    time_minutes = time % 60
    if time < 720:
        am_pm = "AM"
        time_formatted = "%d:%02d" % (time_hours, time_minutes)
    else:
        am_pm = "PM"
        time_formatted = "%d:%02d" % (time_hours - 12, time_minutes)
    return time_formatted + ' ' + am_pm


def convert_to_minutes(time):
    parsed = time.split(':')
    hours = parsed[0]
    parsed2 = parsed[1].split(' ')
    minutes = parsed2[0]
    am_pm = parsed2[1]

    time_in_minutes = float(hours) * 60 + float(minutes)
    if am_pm.upper() == 'AM':
        return time_in_minutes
    elif am_pm.upper() == 'PM':
        return time_in_minutes + 720