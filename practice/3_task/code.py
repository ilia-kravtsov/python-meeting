def get_hours_and_minutes(time_string):
    splitted = time_string.split(':')
    hours = int(splitted[0])
    minutes = int(splitted[1])
    return hours, minutes

time_str = '12:35'
hours, minutes = get_hours_and_minutes(time_str)
print(hours, minutes)