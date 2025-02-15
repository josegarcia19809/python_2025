play_list = {
    "title": "patagonia bus",
    "author": "jose garcia",
    "songs": [
        {"title": "Ecos del Ayer", "artist": ['blue'], "duration": 2.5},
        {"title": "Sombras en la Luna", "artist": ['kitty', "djcat"], "duration": 5.25},
        {"title": "Latidos Perdidos", "artist": ['garfield'], "duration": 2.0},
    ]
}
print("-" * 100)
print(play_list)
print("-" * 100)

duration_total = 0
for song in play_list["songs"]:
    duration_total += song["duration"]

print(duration_total)
print("-" * 100)
for song in play_list["songs"]:
    print(f"The song {song['title']} is played by ")
    for artist in song["artist"]:
        print(f"- {artist}")

    print()
