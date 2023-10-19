from collections import deque

bites = int(input('Numbers of bites:'))
text = input().lower()
names = deque()

while text != 'start':
    names.appendleft(text)
    text = input().lower()

while text != 'end':
    text = input()
    if text == 'end':
        break

    elif text.startswith('refill'):
        bites += int(text.split(' ')[1])

    elif bites >= int(text):
        print(f'{names.pop()} takes bites')
        bites -= int(text)

    elif bites < int(text):
        print(f'{names.pop()} must wait')

print(f'Left {bites} bites')