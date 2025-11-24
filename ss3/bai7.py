def handleReverseTheNumber(number):
    num = 0
    while number > 0:
     digit = number % 10
     num = num * 10 +digit
     number = number // 10
    
    print(f"số sau khi đảo ngược {number} = ")
    return num

print(handleReverseTheNumber(1234))