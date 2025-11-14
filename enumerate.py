my_list=["a","b","c"]
print(list(enumerate(my_list)))

num_list= [1,5,7,9,6,12,3]

for index,num in enumerate(num_list):
    if index % 2 != 0:
        num_list[index]=num * 2
    else:
        num_list[index]=num
print(num_list) 

pizzas = (["Margherita", 7.50], ["Vegetarian", 10.55], ["Meat Lovers", 8.45], ["Hawaiian", 8.3])

for index,(pizza,price) in enumerate(pizzas):
        new_price= round(price*1.15,2)
        pizzas[index][1] = new_price
        print(f"The new price of {pizza} pizza is: {new_price}")


winners = [("William", 1530), ("Elizabeth", 1510), ("Frederick", 1500)]

for index,(name,point) in enumerate(winners,1):
        print(f"{index} - {name} with: {point} points.")
