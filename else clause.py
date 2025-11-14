# ELSE CLAUSE in for loop
for i in range(5,12,2):
    print("LOOP")
    if i==12:
        break
else:
    print("ELSE CLAUSE")

print("=="*25)

# ELSE CLAUSE in while loop
x=5 
while x<10:
    print("LOOP")
    if x==15:
        print("break")
        break
    x+=2
else:
    print("ELSE CLAUSE")

print("=="*25)

def binary_search(sequence,target):
    low=0
    high=len(sequence)-1
    middle=(low+high)//2

    while low<=high:
        if sequence[middle]==target:
            print("Found It!")
            break
        elif sequence[middle]<target:
            low=middle+1
        else:
            high=middle-1
        middle=low+high//2
    else:
        print(f"{target} not found 🥲 🥲")

binary_search("huyert","u")