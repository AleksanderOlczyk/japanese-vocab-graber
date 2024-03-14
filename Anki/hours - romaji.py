def format_hour(hour, minute):
    if minute == 0:
        return f"{hour:02d}:00"
    elif minute == 15:
        return f"{hour:02d}:15"
    elif minute == 20:
        return f"{hour:02d}:20"
    elif minute == 30:
        return f"{hour:02d}:30"
    elif minute == 45:
        return f"{hour:02d}:45"


def convert_to_japanese(hour, minute):
    hour_numbers = {
        1: "ichiji",
        2: "niji",
        3: "sanji",
        4: "yoji",
        5: "goji",
        6: "rokuji",
        7: "shichiji",
        8: "hachiji",
        9: "kuji",
        10: "juuji",
        11: "juuichiji",
        12: "juuniji"
    }

    minute_numbers = {
        0: "",
        5: "gofun",
        10: "jyuppun",
        15: "jyuugofun",
        20: "nijuppun",
        30: "han",
        45: "yonjyuufun"
    }

    if hour == 0:
        hour = 12
    elif hour > 12:
        hour %= 12

    hour_japanese = hour_numbers[hour]
    minute_japanese = minute_numbers[minute]

    if hour < 13:
        return f"gozen {hour_japanese}{' ' if minute != 30 and minute != 0 else ''}{minute_japanese} desu"
    else:
        return f"gogo {hour_japanese}{' ' if minute != 30 and minute != 0 else ''}{minute_japanese} desu"


for hour in range(0, 24):
    for minute in [0, 15, 30, 45]:
        japanese_time = convert_to_japanese(hour, minute)
        print(str(hour) + ":" + str(minute), japanese_time)


with open("japanese_hours.txt", "w") as file:
    file.write("#separator:tab\n")
    file.write("#html:true\n")
    file.write("#tags column:3\n")
    for hour in range(0, 24):
        for minute in [0, 15, 20, 30, 45]:
            formatted_hour = format_hour(hour, minute)
            japanese_time = convert_to_japanese(hour, minute)
            file.write(f"{formatted_hour}\t{japanese_time}\n")