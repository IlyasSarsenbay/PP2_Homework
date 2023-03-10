def multi(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  

print(multi((5,3,6,2,-12)))