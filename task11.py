# Task 11
# 1

# створюємо файл myfile.txt open, 'w'

with open("myfile.txt", "w") as my_file:
    # записуємо в файл Hello file world
    my_file.write("Hello file world!\n")

with open("myfile.txt") as cont_file:
    print(cont_file.read())
