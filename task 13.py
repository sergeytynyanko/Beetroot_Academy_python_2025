# Task 13

# 1
print('Task 13.1')
def func_locals(x, y, z):
    a1 = x * y
    a2 = x * z
    a3 = a1 * a2
    return locals()


vars_inside = func_locals(1, 4, 5)
print('Кількість локальних змінних =', len(vars_inside)) # Кількість локальних змінних = 6

#

# 2
print('Task 13.2')
def multy(a):
    def power(b):
        return (b * 2) ** a
    return power

multy_2 = multy(2)

print('(3 * 2) ** 2 =', multy_2(3))



# 13-3
print('Task 13.3')
def choose_func(nums: list, func1, func2):
    # Перевіряємо, чи всі числа позитивні
    if all(num > 0 for num in nums):
        return func1(nums)  # якщо так — викликаємо першу функцію
    else:
        return func2(nums)  # якщо ні — другу


# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

# Перевірка
assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

print('Перевірки пройдені')
