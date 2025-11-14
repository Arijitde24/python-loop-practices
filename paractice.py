

words = ["bilingual", "macroeconomics", "enlarge", "macroscopic", "monolingual"]

prefix = "macro"
count=0
for i in range(len(words)):
    word_prefix=words[i][:len(prefix)]
    if word_prefix==prefix:
        count+=1
if count>1:
    print(count)


def is_prime(num):
    result=True
    for div in range(2,num):
        if num%div==0:
            result=False
            maxdiv=div
    
    if result:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime. {maxdiv} is a divisor of {num}.")
        

def count_substring(text, substr):
    counter = 0
    for i in range(0, len(text)-len(substr)+1):
        if text[i:i+len(substr)] == substr:
            counter += 1
    print(counter)


def print_winners(winners):
    print("Congratulations! The results are:")

    for i in range(1, len(winners)+1):
        if i == 1:
            print(str(i) + "st", end=" ")
        elif i == 2:
            print(str(i) + "nd", end=" ")
        elif i == 3:
            print(str(i) + "rd", end=" ")
        else:
            print(str(i) + "th", end=" ")
        print("place:", winners[i].capitalize())