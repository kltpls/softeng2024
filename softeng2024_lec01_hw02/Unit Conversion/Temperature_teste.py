def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')




def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_temp = 25
fahrenheit_temp = 77

print(f"{celsius_temp}°C는 {celsius_to_fahrenheit(celsius_temp):.2f}°F입니다.")
print(f"{fahrenheit_temp}°F는 {fahrenheit_to_celsius(fahrenheit_temp):.2f}°C입니다.")




