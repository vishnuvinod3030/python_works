def factorial(num):
    fact=1
    for i in range(1,1+num):
        fact=fact*i
    return fact



def is_leapyear(year):
    if year %100==0 and year %400==0:
        return "leap year"
    elif year %100!=0 and year %4==0:
        return"leap year"
    else:
        return "not leap year"
    
print(is_leapyear(2023))



numbers=10,50,47,56,17
total=sum(numbers)
print(total)



numbers=10,50,47,56,17
largest_num=max(numbers)
print(largest_num)

smallest_num=min(numbers)
print(smallest_num)


