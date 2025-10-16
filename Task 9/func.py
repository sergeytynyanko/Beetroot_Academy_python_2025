# урок 9

# 1

"""
Обчислення площі прямокутника
Обчислення периметру прямокутника
"""


def rectangle1(a, b):
    return a * b


def rectangle2(a, b):
    return 2 * a * b


# ця функція спрацює лише при запуску з цього модуля, якщо з іншого не працює
def main():
    a = int(input("Яка довжина?: >"))
    b = int(input("Яка висота?: >"))
    print("Площа прямокутника = ", rectangle1(a, b))
    print("Периметр прямокутника = ", rectangle2(a, b))


if __name__ == "__main__":
    main()
