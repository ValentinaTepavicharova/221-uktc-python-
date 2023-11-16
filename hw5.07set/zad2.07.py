n = int(input("Enter the number of cars: "))
parked_cars = set()
# празен сет
for _ in range(n):
# цикъла се завърта от 0 до n
    action = input("Enter the car number in the format {IN}/{OUT}, {AAXXXXAA}: ")
    direction, car_number = action.split(", ")
# взимаме action и го разделяме на две променливи direction and car_number
    if direction == "IN":
        parked_cars.add(car_number)
# ако direction е ревно на in номера на колата да се добави в сета
    elif direction == "OUT":
        parked_cars.discard(car_number)
# ако direction е равно на out номера на колата ще се премахне от сето
if parked_cars:
# проверяваме дали има елементи в сета
    for car_number in sorted(parked_cars):
# минаваме през сета и принтираме номерата на колите
        print(car_number)
else:
    print("Parking is empty!")
# ако сета е праен принтираме ,че паркинга е празен
