n = int(input("Enter number:"))
baby_words = set()

for _ in range(n):
    current_words = input("Enter baby words split by space:").split(" ")
    for word in current_words:
        baby_words.add(word)
print(*baby_words, sep='\n')
