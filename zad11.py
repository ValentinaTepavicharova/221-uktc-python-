 names = input().split(' ')
n = int(input())
player = 0

while len(names) > 1:
    player = ((player + n - 1) % len(names))
    print(f"Removed: {names.pop(player)}")
print(f'Last is {names[0]}')
