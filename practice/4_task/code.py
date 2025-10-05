
def check_song_duration(time_string):
    time_list = time_string.split(':')
    minutes_to_seconds = int(time_list[0]) * 60
    seconds = int(time_list[1])
    total_seconds = minutes_to_seconds + seconds
    return total_seconds <= 210


print(check_song_duration('4:35')) # False
print(check_song_duration('2:10')) # True

def get_minutes_and_seconds(time_string):
    time_list = time_string.split(':')
    m = int(time_list[0])
    s = int(time_list[1])
    return m, s


def check_song_duration_2(time_string):
    minutes_and_seconds = get_minutes_and_seconds(time_string)
    minutes_to_seconds = minutes_and_seconds[0] * 60
    seconds = minutes_and_seconds[1]
    total_seconds = minutes_to_seconds + seconds
    return total_seconds <= 210


print(check_song_duration_2('4:35')) # False
print(check_song_duration_2('2:10')) # True

def check_song_duration_3(time_string):
    minutes, seconds = get_minutes_and_seconds(time_string)
    seconds = minutes * 60 + seconds
    return seconds <= 210

print(check_song_duration_2('4:35')) # False
print(check_song_duration_2('2:10')) # True