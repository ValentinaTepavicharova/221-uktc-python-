numbers = input("Enter numbers split by space:").split(' ')
# input взима целият ред ,а split разделя
count = {}
# празен речник
for number in numbers:
# този цикъл минава през всяко число от списъка(numbers )
    if count.get(number) is None:
# number е ключ .get метода ,който взима стойността на ключа is none проверява дали ключа го има в речника
        count[number] = 1
# добавя числото като ключ със стойност защото се среща за 1 път
    else:
        count[number] += 1
# ако го има 1 път да увеличи бройката
for key, value in count.items():
# с този цикъл минаваме през всески ключ(key) и стойност(value) в речника
    print(f" {key} - {value} times ")
