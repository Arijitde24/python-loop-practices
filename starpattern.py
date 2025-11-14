for i in range(4):
    for j in range(2):
        print(i,j)

for i in range(4):
    print("--> Outer Loop")
    for j in range(2):
        print("> Inner Loop")

num_rows=5

"""                       spaces      stars+spaces
    iteration |   i    |num_rows - 1 |    k      |
        1         1        5-1=4          1
        2         2        4-1=3          2
        3         3        3-1=2          3 
        4         4        2-1=1          4
        5         5        1-1=0          5"""




for i in range(1,num_rows+1):
    # SPACES
    for j in range(num_rows-i):
        print(" ",end="")
    # STARS
    for k in range(i):
        print("*",end=" ")
    print()


for i in range(num_rows,0,-1):
    # SPACES
    for j in range(num_rows-i):
        print(" ",end="")
    # STARS
    for k in range(i):
        print("*",end=" ")
    print()

for i in range(num_rows,0,-1):
    # STARS
    for k in range(i):
        print("*",end=" ")
    print()

for i in range(0,num_rows+1):
    # STARS
    for k in range(i):
        print("*",end=" ")
    print()

for i in range(num_rows,0,-1):
    # SPACES
    for j in range(num_rows-i):
        print(" ",end="")
    # STARS
    for k in range(i):
        print("*",end="")
    print()

for i in range(0,num_rows+1):
    # SPACES
    for j in range(num_rows-i):
        print(" ",end="")
    # STARS
    for k in range(i):
        print("*",end="")
    print()