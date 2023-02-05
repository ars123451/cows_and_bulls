from matermind import right_number, get_number, comparison
'''Отгадать одно четырехзначное число с разными цифрами 
       Bulls - количество правильных цифр, стоящих на своём месте
       Сows - количество правильных цифр, стоящих не на своём месте
'''
counter = 0
number = right_number()
# print(right_number())
while True:
    new_number = get_number()
    counter += 1
    cows, bulls = comparison()
    if bulls == 4:
        print('Yes!')
        break
    print('Cows = ', cows)
    print('Bulls = ', bulls)
print(f'It took you {counter} tries')

