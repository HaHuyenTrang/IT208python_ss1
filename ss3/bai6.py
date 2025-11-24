def total_number(number):
    sum = 0
    while number > 0:
     digit = number % 10
     sum += digit
     number = number // 10
    
    print(f"tổng các số trong số {number} = ")
    return sum

print(total_number(1234))