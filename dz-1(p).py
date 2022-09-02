
x, y = int(input("координата x: ")), int(input("координата y: "))
if x > 0 and y > 0:
    print("1-ой четверти")
elif x < 0 and y > 0:
    print("2-ой четверти")
elif x < 0 and y < 0:
    print("3-ей четверти")
elif x > 0 and y < 0:
    print("4-ой четверти")
elif x == 0:
    print("Точка на оси Y")
else:
    print("Точка на оси X")