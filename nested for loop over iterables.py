products={
    "product 1":
        {"brand":"A", 
        "price":5.40},
    "product 2":
        {"brand":"B", 
        "price":7.35},
    "product 3":
        {"brand":"C", 
        "price":2.24},
     }

print("=====================WELCOME TO OUR PRODUCT CATALOGUE======================")
for product,details in products.items():
    print(f"The Product is: {product}")
    for cat,val in details.items():
        print(f"The {cat} is: {val}")
    print("----------------------------------------------------")

    num_iterations=0
    
    for i in range(5):
        print(f"for i= {i}")
        for j in range(8):
            print(f"j = {j}")
            num_iterations += 1




data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list=[]
for i in data:
    temp=[]
    for j in i:
        x=j*10
        temp.append(x)
    new_list.append(temp)
print(new_list)


for i in range (10,0,-1):
    for j in range(i):
        if j%2==0:
            print("*",end=" ")
        else:
            print("-",end=" ")
    print("\n==================")
    