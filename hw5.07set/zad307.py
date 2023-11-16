n = int(input("Enter number of the invitation:"))

invitation = set()
# празен set
for _ in range(n):
# цикъла се завърта от 0 до n
    invitation.add(input())
# добавя поканите в сета
while invitation:
# while върти докато има елементи в сета(invitation)
    command = input("Enter guest number or 'End' to finish: ")
# взимаме поканите от конзолата
    if command == "END":
# да проверим дали имаме командата end
        break
# ако имаме команата end да спре цикъла
    invitation.discard(command)
#  премахваме пристигналите гости от сета
print(sorted(invitation))
# принтираме сета сортиран ,за да учителите да са в началото
print(len(invitation))
# принтираме дължината на сета ,за да видим,кой не е дошъл
