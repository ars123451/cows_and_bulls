from random import randint


def right_number():
    global number
    while True:
        number = str(randint(1234, 9877))
        if number[1] != number[0] and number[2] != number[0] and number[3] != number[0]:
            if number[2] != number[1] and number[3] != number[1]:
                if number[3] != number[2]:
                    number = int(number)
                    break
    return number

def get_number():
    global new_number
    while True:
        new_number = input('Enter your number please: ')
        if new_number.isdigit():
            new_number = int(new_number)
            if 1000 < new_number < 10000:
                break
            else:
                print("Please enter another number! \n")
        else:
            print("Please enter another number! \n")
    return new_number


def comparison():
    global new_number, number, cows, bulls
    new_number = str(new_number)
    number = str(number)
    cows = 0
    bulls = 0
    for value in range(4):
        if new_number[value] in number:
            if new_number[value] == number[value]:
                bulls += 1
            else:
                cows += 1
    return cows, bulls
