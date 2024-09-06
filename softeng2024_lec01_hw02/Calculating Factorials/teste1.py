def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')






def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

num = 5
print(f"{num}! = {factorial(num)}")
