n = int(input())
even_set = set()
odd_set = set()

for i in range(1, n+1):
    name = input("Enter name:")
    sum1 = 0
    for element in name:
        sum1 += ord(element)
    sum1 = sum1//i
    if sum1 % 2 == 0:
        even_set.add(sum1)
    else:
        odd_set.add(sum1)
even_sum = sum(even_set)
odd_sum = sum(odd_set)
if even_sum == odd_sum:
    result1 = even_set.union(odd_set)
    print(*result1, sep='-')
if odd_sum > even_sum:
    result2 = odd_set.difference(even_set)
    print(*result2, sep='-')
if even_sum > odd_sum:
    result3 = even_set.symmetric_difference(odd_set)
    print(*result3, sep='-')

