list=["Vehicle","Noon","Kayak","Child","Anna","Mother","May"]
def list_palindrome(word):
    palindromes=[]
    for elm  in word:
    
        check=(elm[ : :-1])
        if check.lower()!=elm.lower():
            continue
        palindromes.append(elm)

    print(palindromes)

list_palindrome(list)