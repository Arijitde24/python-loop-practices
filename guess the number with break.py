low=0
high=1000
ans= (low + high)//2
print("=========================")
print("   WELCOME TO THE GAME   ")
print("=========================")
print("think of a number between 1 and 1000")
num_iteration=0
while True:
    num_iteration+=1
    print("Enter 1 if ans is too low")
    print("Enter 2 if ans is too high")
    print("Enter 3 if ans is correct")
    print(f"\nIs {ans} the answer")
    user_input=int(input())
    if user_input==1:
        low=ans
        ans=(low+high)//2
    elif user_input==2:
        high=ans
        ans=(low+high)//2
    elif user_input==3:
        print(f"\n FOUND IT the Answer: {ans}")
        if num_iteration==1:
            print("Only 1 iteration needed to find the number")
        else:
            print(f"only {num_iteration} iterations needed to find the number")
        break
        
    else:
        print("invalid input")
