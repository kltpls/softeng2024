def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')





    even_numbers = [num for num in range(1, 101) if num % 2 == 0]
    total_sum = sum(even_numbers)
    print(total_sum)
