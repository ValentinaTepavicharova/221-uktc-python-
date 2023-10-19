from collections import deque

def hot_potato(children, n):
    circle = deque(children.split())
    
    while len(circle) > 1:
        for _ in range(n - 1):
            circle.append(circle.popleft())
        
        removed_child = circle.popleft()
        print(f"Removed {removed_child}")
    
    winner = circle.pop()
    print(f"Winner is {winner}")

names = input("Enter the children's names separated by a space: ")
nth_throw = int(input("Enter the nth throw: "))

hot_potato(names, nth_throw)