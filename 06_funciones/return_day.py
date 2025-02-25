"""
return_day
Write a function called return_day. this function takes in one parameter
(a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is
Tuesday etc.). If the number is less than 1 or greater than 7, the function should
return None

Hint: store the days of the week in a list (or dict using numbers as keys).
"""


def return_day(day: int):
    days: dict[int, str] = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",

    }
    if day not in days:
        return None
    return days[day]


print(return_day(1))
print(return_day(3))
print(return_day(5))
print(return_day(7))
print(return_day(78))

"""
Here's a solution that uses what we've learned so far.  

Keep track of the days in a list.  
Check to make sure num isn't < 0 or  > 6.  
Return the corresponding day. Use days[num-1] because return_day(1) should return 
0th item in list.
"""


def return_day2(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # Check to see if num valid
    if 0 < num <= len(days):
        # use num - 1 because lists start at 0
        return days[num - 1]
    return None


"""
BONUS ADVANCED VERSION:

Here's a more advanced solution that involves error handling, which we have not 
covered yet.  It eliminates the need to check to see if num is a valid index in the 
list. We cover this in the debugging section, but I thought you may want to see if now.
"""


def return_day3(num):
    try:
        return \
        ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][
            num - 1]
    except IndexError as e:
        return None
