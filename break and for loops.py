print("Let's find a letter in a string: ")
text=input("Enter the string: \n")
target= input("Enter the letter: \n")
for char in text:
    print("----> Searching")
    if char==target:
        print("Found It!")
        break
