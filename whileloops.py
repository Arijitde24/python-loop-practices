i=0
while i<=5:
    print(i)
    i+=1

print("="*50)

valid_input = False
while not valid_input:
    user_input = input("Please enter a number: ")
    if user_input.isnumeric():
        valid_input = True
    else:
        print("Please enter a valid input")

print("="*50)

# infinite loop the condition is never false
"""i=0
while i<=5:
    print(i)"""
# infinite loop can only be stopped using(ctrl + c)in keyboard or due to insuffecient space3

x=5
while x>=0:
    print(x)
    x-=1
print("END")
print("="*50)

continue_loop=True
while continue_loop:
    print("Enter 2 integers")
    num1=int(input("integer 1:\n"))
    num2=int(input("integer 2:\n "))
    print(f"{num1} + {num2} = {num1+num2}")
    print("want to enter 2 new integer")
    ans=input("enter yes or no: \n")
    if ans=="no":
        continue_loop=False

print("="*50)