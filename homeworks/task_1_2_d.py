import random
from datetime import timedelta


def generate_song():
    minute_length = random.randint(3,8)
    second_length = random.uniform(0.0, 0.59)
    return round(minute_length + second_length, 2)


songs = [generate_song() for i in range(3)]
times = [timedelta(minutes=int(song), seconds=int(str(song).split('.')[1])) for song in songs]
total_duration = sum(times, timedelta())
total_minutes = total_duration.seconds // 60
total_seconds = total_duration.seconds % 60

print(songs)
print(f"Три песни звучат {total_minutes}.{total_seconds} минут")