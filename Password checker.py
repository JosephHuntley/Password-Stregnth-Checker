import re

def regexp_check(regexp, text, msg):
    if regexp.search(text):
        print(f'{msg}: Passed')
        return 1
    else:
        print(f'{msg}: Failed')
        return 0

def strength_checker(text):
    uppercase = re.compile('[A-Z]')
    lowercase = re.compile('[a-z]')
    numbers = re.compile('[1-9]')
    special = re.compile('[!|@#$%^&()_+=-{}/]')

    if len(text) >= 12:
        points = 2
        print('Length: Passed')
    elif len(text) >= 8:
        points = 1
        print('Length: Failed')
    else:
        points = 0
        print('Length: Failed')

    points += regexp_check(uppercase, text, "Uppercase")
    points += regexp_check(lowercase, text, "Lowercase")
    points += regexp_check(numbers, text, "Numbers")
    points += regexp_check(special, text, "Special")
    return points


password = input('What is your current password?\n')
points = strength_checker(password)
if points == 6:
    print('You have a strong password')
elif points in range(4,6):
    print('You have a good password, but there is room for improvment.')
elif points in range(1,4):
    print('You have a weak password')
