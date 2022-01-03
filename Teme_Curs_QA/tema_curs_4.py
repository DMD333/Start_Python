# 1 - Write a Python program to find the number of days in a month.
# Test Data
# Input a month number: 2
# Input a year: 2016
# Expected Output :
# February 2016 has 29 days
def months(argument):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
def month():
    luna = int(input('Insert number between 1 to 12: '))
    an = int(input('insert year: '))

    if luna == 2 and (an % 4 == 0 or an % 400 == 0):
        print(f'February {an} has 29 days')
    elif luna % 2 != 0 or luna == 7:
        print(f'{months(luna)} {an} has 31 days')
    else:
        print(f'{months(luna)} {an} has 30 days')
month()

# 2 - Write  a Python program to find the zodiacal sign when you have the day
# and  the month of birth
# Test Data
# Input a month : november
# Input a day: 19
# Expected Output :
# Your zodiac sign is :Scorpio
def zodiac_sign():
    day = int(input('Insert day number between 1 to 31: '))
    luna = int(input('insert month: '))

    if luna == 1 and 20 <= day <= 31 or luna == 2 and 1 <= day <= 19:
        print("Aquarius")
    elif(luna == 2 and 20 <= day <= 29) or (luna == 3 and 1 <= day <= 20):
        print("Pisces")
    elif(luna == 3 and 21 <= day <= 31) or (luna == 4 and 1 <= day <= 20):
            print("Aries")
    elif (luna == 4 and 21 <= day <= 30) or (luna == 5 and 1 <= day <= 20):
        print("Taurus")
    elif(luna == 5 and 21 <= day <= 31) or (luna == 6 and 1 <= day <= 20):
        print("Gemini")
    elif (luna == 6 and 21 <= day <= 30) or (luna == 7 and 1 <= day <= 22):
        print("Cancer")
    elif (luna == 7 and 23 <= day <= 31) or (luna == 8 and 1 <= day <= 22):
        print("Leo")
    elif (luna == 8 and 23 <= day <= 31) or (luna == 9 and 1 <= day <= 22):
        print("Virgo"),
    elif (luna == 9 and 23 <= day <= 31) or (luna == 10 and 1 <= day <= 22):
        print("Libra")
    elif (luna == 10 and 23 <= day <= 31) or (luna == 11 and 1 <= day <= 22):
        print("Scorpio")
    elif (luna == 11 and 23 <= day <= 31) or (luna == 12 and 1 <= day <= 21):
        print("Sagittarius")
    elif (luna == 12 and 21 <= day <= 31) or (luna == 1 and 1 <= day <= 19):
        print("Capricorn")

zodiac_sign()


# 3 - Write a program in Python to display the first 10 natural numbers.
def natural():
    for x in range(0, 10):
        print(x+1)

natural()

# 4 - Write a program in Python to display first the sum and the average of
# numbers from 200 to 450.
def sum_and_average():
    count = 0
    sum = 0
    average = 0
    for x in range(200, 450):
        count += 1
        sum += x
        average = sum / count
    print(f'suma = {sum} iar Media este {average}')

sum_and_average()