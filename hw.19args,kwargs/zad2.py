def sum_func(*args):
    sum = 0
    for number in args:
        if number % 2==0:
            sum+=number
    return sum

print(sum_func(1, 4, 5))
print(sum_func(4, 5, 6, 1, 3))
print(sum_func(2, 20, 10, 15, 28, 3, 1))
