from matermind import right_number, get_number, comparison

counter = 0
number = right_number()
print(right_number())
while True:
    new_number = get_number()
    counter += 1
    cows, bulls = comparison()
    if bulls == 4:
        print('Yes!')
        break
    print('cows = ', cows)
    print('Bulls = ', bulls)
print(f'It took you {counter} tries')

