# урок 8

# 1
def favorite_movie(name):
    print(f'Мій улюблений фільм називається - {name}')

movie = 'Back to Future'
favorite_movie('Назад у майбутне') # Мій улюблений фільм називається - Назад у майбутне
favorite_movie(movie) # Мій улюблений фільм називається - Back to Future

# 2
def make_country(name, capital):
    dict_country[name] = capital
    print(dict_country)

dict_country = {}
make_country('Україна', 'Київ') # {'Україна': 'Київ'}
make_country('Греція', 'Афіни')
make_country('Бельгія', 'Брюссель')

# 3
def make_operation(operand, *argum):
    func_result = argum[0]
    for i in argum[1: len(argum)]:

        if operand == '+':
            func_result = func_result + i
        elif operand == '-':
            func_result = func_result - i
        elif operand == '*':
            func_result = func_result * i
        else:
            print('Невірний оператор')
    print('Результат дорівнює = ', func_result)

make_operation('+', 7, 7, 2) # Результат дорівнює =  16
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 6)


