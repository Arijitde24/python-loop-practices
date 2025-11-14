print(zip())
print(list(zip()))
print(list(zip([1,2,3,4])))
print(list(zip([1,2,3,4],[5,6,7,8])))
print(list(zip([1,2],[3,4],[5,6])))

a=[1,2]
b=[3,4]
c=[5,6]
print(list(zip(a,b,c)))

print(list(zip([1,2,3],[4,5],[6,7,8,9])))

months=["January","February","March"]
first_product=[530,343,670]
second_product=[250,210,295]
third_product= [715,652,850]

for month,a,b,c in zip(months,first_product,second_product,third_product):
    total= a + b + c
    print(f"Total reveneue for the {month} is: {total}")

first_list=[1,2,3,4]
second_list=[5,6,7]

for num1,num2 in zip(first_list,second_list):
    print(num1,num2)


first_dict = {"A": 10, "B": 25, "C": 13}
second_dict = {"A": 12, "B": 45, "C": 89}

for (key1, val1), (key2, val2) in zip(first_dict.items(), second_dict.items()):
    print(key1, val1, " / ", key2, val2)

for val1, val2 in zip(first_dict.values(), second_dict.values()):
    print(val1, "-", val2)

for k1, k2 in zip(first_dict.keys(), second_dict.keys()):
    print(k1, "-", k2)

category = ["red", "green", "blue"]
color = [235, 150, 2]
print(dict(zip(category,color)))


str1 = "aabbcccddee"
str2 = "aaabccddeee"

dupli=0

for x,y in zip(str1,str2):
    if x==y:
        dupli+=1
    else:
        dupli+=0
print(dupli)


chars = ["*", "-", "#", "="]
repetitions = [5, 4, 3, 2]

for char, rep in zip(chars, repetitions):
    print(char * rep)



listA = [(1, "A"), (2, "b"), (3, "C"), (4, "e")]
listB = [(1, "a"), (2, "b"), (3, "C"), (6, "f")]


for x,y in zip(listA,listB):
    if x==y:
        print("Equal")
    else:
        print("Not Equal")