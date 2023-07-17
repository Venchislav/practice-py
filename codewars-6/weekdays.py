weekdays = {1: "Sunday",
            2: "Monday",
            3: "Tuesday",
            4: "Wednesday",
            5: "Thursday",
            6: "Friday",
            7: "Saturday"}

err = "Wrong, please enter a number between 1 and 7"


def whatday(num):
    return weekdays[num] if 1 <= num <= 7 else err
