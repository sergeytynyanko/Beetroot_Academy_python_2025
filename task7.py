# урок 7
import random

# Завдання 1

user_string = input("string - ") 
print(user_string)

a_list = user_string.split()
print('a_list - ', a_list)

a_dict = {}

for key in a_list:
    a_dict[key] = (a_list.count(key))   

print(a_dict) 


    
# Завдання 2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
summ = {}

for i in stock.keys():
    summ[i] = stock[i] * prices[i]

print(summ)



# Завдання 3


double_list = []
for i in range(1, 11):
    double_list.append((i, i ** 2))

print(double_list)


# Завдання 4

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days1 = {}
days2 = {}
for i, day in enumerate(days):
    days1[day] = (i + 1)
    days2[i + 1] = (day)

print(days1)
print(days2)

