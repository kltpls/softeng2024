def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')




total_sum = 0
for num in range(1, 101):
    if num % 2 == 0:
        total_sum += num
print(total_sum)
