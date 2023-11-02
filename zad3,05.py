from collections import deque
food=int(input())
#konstruktora , koyato priema list
orders=deque([int(i) for i in input().split(" ")])
print(max(orders))
#ako hranata e poveche shte se izpulnqt poruchkite
if sum(orders)<=food:
    print("Orders complete")
else:
    while food > 0:
#vadim wsyaka poruchka i kato ostane q printirame
        food-=orders.popleft
    print(f"Left orders:{orders} " )
