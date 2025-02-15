# access_data_artist.py
# Access Data in a Dictionary Exercise
# Given the dictionary below:
#
# artist = {
#     "first": "Neil",
#     "last": "Young",
# }
# Declare a variable called full_name that is equal to artist's first  and last  names with a space between.
# You must reference the values associated with those keys in the artist dictionary.
#
# print(full_name)
# # Neil Young

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist["first"] + " " + artist["last"]
print(1, full_name)

full_name2 = "{} {}".format(artist["first"], artist["last"])
print(2, full_name2)

full_name3 = f"{artist['first']} {artist['last']}"
print(3, full_name3)
