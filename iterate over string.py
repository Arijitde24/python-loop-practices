my_string="Learning Loops"
new_string=""
for i in my_string:
    if i.isupper():
        new_string+=i.lower()
    else:
        new_string+=i.upper()
print(new_string)

ms="aaabbcccddeffghhii"
ns=""
for i in ms:
    if i not in ns:
        ns+=i
print(ns)