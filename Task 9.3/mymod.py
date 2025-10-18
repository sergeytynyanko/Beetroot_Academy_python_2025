# Підраховує кількість рядків
def count_lines(content):
    # на початок файлу
    content.seek(0)
    # Підраховує кількість рядків у вже відкритому файлі.
    lines = len(content.readlines())
    # повертає кількість рядків
    return lines


def count_chars(content):
    # на початок файлу
    content.seek(0)
    # Підраховує кількість символів у файлі
    text = len(content.read())
    return text


def test(name):
    with open(name) as f_cont:
        lines = count_lines(f_cont)
        chars = count_chars(f_cont)
        print(f"Файл: {name}")
        print(f"Рядків: {lines}")
        print(f"Символів: {chars}")


# test("weekdays.txt")

# Якщо модуль запускається як головний
if __name__ == "__main__":
    test("mymod.py")
