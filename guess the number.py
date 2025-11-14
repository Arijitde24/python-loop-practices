import random
target_num=random.randint(1,1000)
print(target_num)
num_guesed=False
while not num_guesed:
    user_num= int(input("Enter a number between 1 and 1000: \n"))
    if user_num==target_num:
        print("Correct")
        num_guesed=True
    elif user_num<target_num:
        print("Higher")
    elif user_num>target_num:
        print("Lower")