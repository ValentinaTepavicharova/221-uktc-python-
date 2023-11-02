from collections import deque
food=int(input())
orders=deque([int(i) for i in input().split(" ")])
print(max(orders))
if sum(orders)<=food:
    print("Orders complete")
else:
    while food > 0:
        food-=orders.popleft
    print(f"Left orders:{orders} " )
