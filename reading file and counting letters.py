import pprint

letter_freq={}

with open("Metamorphosis+by+Franz+Kafka.txt","r") as file:
    for line in file:
        for word in line.split():
            for letter in word:
                if letter.isalpha():
                    if letter.lower() in letter_freq:
                        letter_freq[letter.lower()]+=1
                    else:
                        letter_freq[letter.lower()]=1


print(f"Most Frequent Letter is: {max(letter_freq,key=letter_freq.get)}")
print()
print("Frequency: ")
pprint.pprint(letter_freq)