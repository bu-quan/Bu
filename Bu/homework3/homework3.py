def say_goodbye(name):
    print("Goodbye", name)


def circle_area(radius):
    print(3.14*pow(radius,2))


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def temperature_range_manual(temperatures):
    min_temp = temperatures[0]
    max_temp = temperatures[0]
    
    for temp in temperatures:
        min_temp=min(min_temp,temp)
        max_temp=max(max_temp,temp)            
    return (min_temp, max_temp)

def is_weekend(day):
    return day==6 or day==7

def fuel_efficiency(distance, fuel_used):
    return distance / fuel_used


def encrypt_number(number):
    num_str = str(number)
    if len(num_str) == 1:
        return number
    encrypted_str = num_str[-1] + num_str[:-1]
    return int(encrypted_str)

def power(x,y):
    total=1
    for a in range(y):
        total*=x
    return total

def find_min_for(numbers):    
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def find_max_for(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def find_min_while(numbers):
    min_val = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] < min_val:
            min_val = numbers[i]
        i += 1
    return min_val

def find_max_while(numbers):
    max_val = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > max_val:
            max_val = numbers[i]
        i += 1
    return max_val

def sum_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

x=8
y=6
result = power(x, y)
print(f"The result of Oski Stole Your Power (5.1) with x = {x} and y = {y} is {result}.")