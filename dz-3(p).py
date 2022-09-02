firstPoint= list(map(int, input("точки x y z:").split()))
secondPoint= list(map(int, input("x y z :").split()))
result = (((secondPoint[0] - firstPoint[0])**2) + ((secondPoint[1] - firstPoint[1])**2) + ((secondPoint[2] - firstPoint[2])**2))**(1/2)
print(f"Расстояние между двумя точками = {round(result, 2)}")