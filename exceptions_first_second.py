example = str(input('Введите выражение: '))
spl_example = example.split(' ')
sign = spl_example[0]
first = spl_example[1]
second = spl_example[2]
assert sign in ['+', '-', '*', '/'], 'Вы ввели неверный знак!'
try:
    if sign == '+':
        print(int(first) + int(second))
    elif sign == '-':
        print(int(first) - int(second))
    elif sign == '*':
        print(int(first) * int(second))
    elif sign == '/':
        try:
            result = int(first) / int(second)
        except ZeroDivisionError:
            result = first
            print('На ноль делить нельзя!')
except ValueError:
    print('Вы ввели что-то другое, не число!')