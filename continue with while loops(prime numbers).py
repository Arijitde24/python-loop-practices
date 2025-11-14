import math

def divisors(num):
    divisors_list=[1,num]
    divisor=2
    while divisor<=math.sqrt(num):
        if num%divisor==0:
            divisors_list.append(divisor)
            divisors_list.append(num//divisor)
        divisor+=1
    return sorted(list(set(divisors_list)))

while True:
    value=input("Enter the number to find whether it is prime or not, type 's' to stop: \n")
    if value=='s':
        break
    elif (not value.isnumeric()) or ((int(value))<=0):
        print("Enter a valid input")
        continue
    div=divisors(int(value))
    if len(div)==2:
        print(f"The number {value} is prime")
    else:
        print(f"The number {value} is not prime")
        print(f"Divisors: {div}")
