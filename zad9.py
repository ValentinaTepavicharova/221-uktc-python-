from collections import deque 

#добавяне на клас deque от пакета collections 

my_deque=deque()
#конструктора
customer=""

while  customer != "END":
    
    customer = input("Enter customer name(or ‘END’ for the last people in the line): ")
    
#Докато човека не напише End конзолата работи ,но ако е въведено End конзолата спира и пише това ,което и е било зададено до момента

    if customer == "END":
        break
    elif customer == "PAID":
        for person in my_deque:
            print(person)
        my_deque.clear()
    else:
        my_deque.append(customer)

print(f"Left people in the line : {len(my_deque)} people.")