import random

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
songs = random.sample(my_favorite_songs, 3)
minutes = sum(int(song[1]) for song in songs)
seconds = sum(song[1] % 1 for song in songs)
total_minutes = minutes + seconds // 0.6
total_seconds = seconds % 0.6
total_time = round(total_minutes + total_seconds, 2)
print(f"Три песни звучат {total_time} минут")