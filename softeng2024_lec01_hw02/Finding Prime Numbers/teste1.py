def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')




def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_primes_up_to(max_num):
    primes = []
    for num in range(2, max_num + 1):
        if is_prime(num):
            primes.append(num)
    return primes


max_num = 50
print(f"1부터 {max_num}까지의 소수: {find_primes_up_to(max_num)}")
