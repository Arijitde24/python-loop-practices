for i in range(2,4):
    for j in range(2):
        if (i+j)%2==0:
            continue
        print(i,j)

my_words = ["Python", "Loops", "While", "For", "Break", "Continue"]
 
for word in my_words:
    if "e" in word:
        continue
    print(word.lower())


i = 1

while i <= 3:
    j = 1
    while j <= 5:
        if j == 3:
            j += 1
            continue  # skip the rest and go to next j
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1