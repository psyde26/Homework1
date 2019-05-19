first_line = input('Введите первую строку: ')
second_line = input('Введите вторую строку: ')


def length_of_lines(line1, line2):
    if type(line1) is not str or type(line2) is not str:
        return('0')
    elif len(line1) == len(line2):
        return('1')
    elif len(line1) > len(line2):
        return('2')
    elif len(line1) != len(line2) and line2 == ('learn'):
        return('3')
    

result = length_of_lines(first_line, second_line)
print(result)