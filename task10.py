# Task 1

def oops(x):
    print(x[len(x)])

y = [1, 2, 3, 4, 5]
# oops(y)

try:
    oops(y)
# except KeyError:
except IndexError:
    print('Error')
# Як що замінити IndexError на KeyError,
# програма зупинить роботу та видасть помилку: IndexError: list index out of range


# Task 2

def qwad(a, b):
    #
    try:
        result = a ** 2 / b
    except TypeError:
        print("Введені не числа")
        
    except ZeroDivisionError:
        print("Не можна ділити на нуль")

    else:
        print(result)
    finally:
        result = "End function"
        return  result


a = input('Введіть число a:')
b = input('Введіть число b:')
print(qwad(a, b))
print(qwad(5, 0))
print(qwad(5, 3))



a = input('Введіть число a:')
b = input('Введіть число b:')
print(qwad(a, b))
print(qwad(5, 0))
print(qwad(5, 3))
