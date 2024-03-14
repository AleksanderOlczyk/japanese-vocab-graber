def generate_numbers_with_japanese(start, end, step=1):
    numbers = []
    current = start

    while current <= end:
        numbers.append((current, convert_to_japanese(current)))
        current += step

    return numbers


def convert_to_japanese(number):
    japanese_numbers = {
        0: 'zero', 1: 'ichi', 2: 'ni', 3: 'san', 4: 'yon', 5: 'go',
        6: 'roku', 7: 'nana', 8: 'hachi', 9: 'kyuu', 10: 'juu',
        11: 'juuichi', 12: 'juuni', 13: 'juusan', 14: 'juuyon', 15: 'juugo',
        16: 'juuroku', 17: 'juunana', 18: 'juuhachi', 19: 'juukyuu', 20: 'nijuu',
        30: 'sanjuu', 40: 'yonjuu', 50: 'gojuu', 60: 'rokujuu', 70: 'nanajuu',
        80: 'hachijuu', 90: 'kyuujuu'
    }

    if number in japanese_numbers:
        return japanese_numbers[number]
    elif number < 100:
        tens = number // 10 * 10
        ones = number % 10
        return f"{japanese_numbers[tens]}{' ' + japanese_numbers[ones] if ones != 0 else ''}"
    elif number < 1000:
        hundreds = number // 100
        remainder = number % 100
        return f"{japanese_numbers[hundreds]} hyaku{' ' + convert_to_japanese(remainder) if remainder != 0 else ''}"
    elif number == 1000:
        return 'sen'


numbers_1_to_100 = generate_numbers_with_japanese(1, 99)
numbers_100_to_1000 = generate_numbers_with_japanese(100, 1000, 12)

for number, japanese_translation in numbers_1_to_100:
    print(f"{number}: {japanese_translation}")

for number, japanese_translation in numbers_100_to_1000:
    print(f"{number}: {japanese_translation}")


with open("japanese_numbers.txt", "w") as file:
    file.write("#separator:tab\n")
    file.write("#html:true\n")
    file.write("#tags column:1\n")
    for number, japanese_translation in numbers_1_to_100:
        file.write(f"{number}\t{japanese_translation}\n")
    for number, japanese_translation in numbers_100_to_1000:
        file.write(f"{number}\t{japanese_translation}\n")