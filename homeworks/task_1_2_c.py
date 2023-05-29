import random

def generate_song():
    minute_length = random.randint(3,8)
    second_length = random.uniform(0.0, 0.59)
    return round(minute_length + second_length, 2)


songs = [generate_song() for i in range(3)]
minutes = sum(int(song) for song in songs)
seconds = sum(song % 1 for song in songs)
total_minutes = minutes + seconds // 0.6
total_seconds = seconds % 0.6
total_time = round(total_minutes + total_seconds, 2)
print(songs)
print(f"Три песни звучат {total_time} минут")