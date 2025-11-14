my_list=["bb","ddd","z"]
print(sorted(my_list,key=len))

print("="*50)

for x in sorted(my_list,key=len):
    print(x)    

print("="*50)

print(sorted(["d", "a", "A", "B", "b", "c"], key=str.lower))

print("="*50)

my_list1=[2,1,0,8,3]
print(sorted(my_list1))

print("="*50)

my_tuple=(2,1,0,8,3)
print(sorted(my_tuple,reverse=True))

print("="*50)

my_dictionary={"Z":5,"X":10,"A":8,"D":15}

print(sorted(my_dictionary))

print("="*50)

print(sorted(my_dictionary.values()))

print("="*50)

loops="python"
print(sorted(loops))

print("="*50)

list_tuples=[("A",5),("B",8),("C",0),("D",9)]
def get_last_elm(item):
    return(item[-1])

for char,num in sorted(list_tuples,key=get_last_elm):
    print(char,num)

print("="*50)

for char,num in sorted(list_tuples,key=lambda item:item[-1]):
    print(char,num)

print("="*50)

distances = {
    "A": 342,
    "B": 653,
    "C": 231,
    "D": 684,
    "E": 1232,
    "F": 214
}

for val in sorted(distances.values()):
    print(val)

print("="*50)

for city in sorted(distances):
    print(city)

print("="*50)

for city in sorted(distances, reverse=True):
    print(city)

print("="*50)

s="HELLO, World!"
for char in reversed(s):
    print(char)

print("="*50)

my_list_2= [6,8,9,3,1,7]
print(list(reversed(my_list_2)))

print("="*50)

for i in reversed(my_list_2):
    print(i)

print("="*50)

my_dictionary={
    "Z" : 5,
    "A" : 10,
    "C" : 15,
    "M" : 6
}
print(list(reversed(my_dictionary)))

print("="*50)

print(list(reversed(my_dictionary.values())))

print("="*50)

print(list(reversed(my_dictionary.items())))

print("="*50)


numbers = [5, 15, 7, 4, 8, 12, 9, 3]
even_numbers = 0

for num in reversed(numbers):
    if num % 2 == 0:
        even_numbers += num
    else:
        even_numbers +=0
print(even_numbers)


print("="*50)


posts = {
    "2354": {
        "user": "Python51",
        "content": "I really like this",
        "likes": 35
    },
    "2355": {
        "user": "Loops55",
        "content": "Awesome",
        "likes": 123
    },
    "2356": {
        "user": "Coder58",
        "content": "This is really good",
        "likes": 27
    }
}

def get_likes(post):
    return post["likes"]

def display_sorted_posts(posts):
    for post_id, post_data in sorted(posts.items(), key=lambda item: get_likes(item[1])):
        print(f"Post ID: {post_id}, User: {post_data['user']}, Content: {post_data['content']}, Likes: {post_data['likes']}")

display_sorted_posts(posts)