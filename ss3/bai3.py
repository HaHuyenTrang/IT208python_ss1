def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *=i
        
    print(f"n! = {num} ")  
    
    return n
        
print(factorial(5))
        