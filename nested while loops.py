i=1
while i<=4:
    j=0
    while j<=2:
        print(i,j)
        j+=1
    i+=1

print("="*50)

i=1
while i<=5:
    j=1
    while j<=i:
        print((i*2),end=" ")
        j+=1
    print()
    i+=1

print("="*50)

for i in range(4):
    k = 0
 
    while k < 7:
        print(i, k)
        k += 2
print("="*50)


i = 8
while i >= 1:
    j = 1
    while j <= i:
        if i % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
        j += 1
    print()  # New line after each row
    i -= 1



