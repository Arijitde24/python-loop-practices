for i in range(1,1001):
    print(i)

for i in range(4):
    print(i)

import sys

sequence=[i for i in range(1,1001)]
print(sys.getsizeof(sequence))

range_sequence=range(1,1001)
print(sys.getsizeof(range_sequence))
# SIZE OF LIST is more than RANGE so range is sometimes more preferable than list

print(list(range(5)))
print(list(range(-5)))

for i in range(5):
    print(i+2)

result=0
for i in range(1,11):
    result+=i
print(result)

vowels=["a","e","i","o","u"]
for i in range(len(vowels)):
    print(vowels[i].upper())

numbers=[2,3,4,5]
for i in range(len(numbers)):
    numbers[i]=(numbers[i]*2)
print(numbers)

numbers=[2,3,4,5]
for i in numbers:
    if i%2==0:
        print("EVEN")
    else:
        print("ODD") 

word='madam'
is_palindram=True

for i in range(len(word)//2):
    left_char=word[i]
    right_char=word[len(word)-i-1]
    if left_char.lower()!=right_char.lower():
        is_palindram=False
print(is_palindram)

product=1
for i in range(1,11):
    product*=1*i
print(product)

word="programming"
for i in range(1,len(word) -2):
    print(word[i:i+2])

for i in range(2,10,2):
    print(i)

print(list(range(5,20,6)))

word="HELLO WORLD"
for i in range(1,len(word),2):
    print(word[i])

n=50
odd_numbers=[]
for i in range(1,n,2):
    odd_numbers.append(i)
print (odd_numbers)

print(list(range(-10,-20)))

print(list(range(-10,-20,-1)))

text = "Python Loops"
 
for i in range(len(text)-1, -1, -1):
    print(text[i])