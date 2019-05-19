age = int(input('Введите Ваш возраст: '))


def your_age(age):
    if age <= 7:
        return('Вам в детский сад')
    elif age <= 18:
        return('Вам в школу')
    elif age <= 25:
        return('Вам в ВУЗ')
    elif age > 25:
        return('Вам на работу')


result = your_age(age)
print(result)