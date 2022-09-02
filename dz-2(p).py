number = int(input("номер четверти (от 1 до 4): "))
if number == 1:
    print(f"Допустимые {number} четверти: x > 0, y > 0")
elif number == 2:
    print(f"Допустимые {number} четверти: x < 0, y > 0")
elif number == 3:
    print(f"Допустимые {number} четверти: x < 0, y < 0")
elif number == 4:
    print(f"Допустимые {number} четверти: x > 0, y < 0")
else:
    print("Неправильно!")