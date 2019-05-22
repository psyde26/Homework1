def get_summ(num_one, num_two):
    try:
        return int(num_one) + int(num_two)   
    except(ValueError):
        return 'Я так не умею'

result = get_summ(input('Введите первое число:  '), input('Введите второе число:  '))
print(result)