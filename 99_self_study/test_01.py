def positive_sum(numbers):
    result = 0
    for i in numbers:
        if i>0:
            result += i
    return result

print(positive_sum([1, -4, 7, 12])) 
print(positive_sum([-1, -2, -3, -4]))
