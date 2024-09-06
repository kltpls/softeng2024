def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')



def check_odd_even(number):
    if number % 2 == 0:
        return "짝수"
    else:
        return "홀수"

num = 7
print(f"{num}은 {check_odd_even(num)}입니다.")
