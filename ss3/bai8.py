number = int(input("nhập 1 số nguyên: "))
def PerfectNumber(number):
    sum = 0
    for i in range(1,number):
        if number % i == 0:
            sum += i   
            
    if number == sum:
        print(f"{number} là số hoàn hảo")  
    else:
        print(f"{number} không phải số hoàn hảo")   
    return number == sum

print(PerfectNumber(number))