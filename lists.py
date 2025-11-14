my_list=["a","b","c"]
print(my_list)
print(my_list[0])

numbers=[1,2,3]
numbers.append(4)
print(numbers)
numbers.insert(2,5)
print(numbers)

colors=['purple','blue','green','purple']
colors.remove('purple')
print(colors)
index=colors.index('green')

my_list = [8, 4, 7, 2, 6, 3, 9]
print(my_list[4::2])
print(my_list[::-1])
print(my_list[:5])
print(my_list[4:9])
print(my_list[5:1000]) # Try this one. What do you see?
print(my_list[2:6])

programming_languages=["Python","Javascript","C++","Kotlin"]
print(programming_languages)
print(programming_languages[0])
print(programming_languages[0][0])
print(len(programming_languages))
print(len(programming_languages[1]))
print(programming_languages[1:3])
print(programming_languages[ : :-1])
print(programming_languages[ : :2])
programming_languages.extend(["Swift","Java"])
print(programming_languages)
programming_languages.sort()
print(programming_languages)
programming_languages.reverse()
print(programming_languages)

print([1,2,3] + [4,5,6])

nested_lists=[['a','b','c'],['d','e']]
print(nested_lists)
print(nested_lists[0])
print(nested_lists[0][2])