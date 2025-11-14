my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
 
for seq in my_list:
    for elem in seq:
        if elem > 5:
            print("Found it!")
        break

print("="*50)


grades={}

print("================Student and Grades================")
while True:
    
    while True:
        first_name=input("Enter The First Name Of The Student: \n").strip()
        last_name=input("Enter The Last Name Of The Student: \n").strip()
        if first_name.isalpha() and (last_name.isalpha() or last_name == ""):
             name=first_name+" "+last_name
             break
        else:
            print("INVALID INPUT! Please Enter a Valid name(HINT:- only ALPHABETS)")
    
    while True:
        grade=input("Enter The Grade Of The Student: \n")
        if grade.isnumeric() and 0<=int(grade)<=100:
            break
        else:
            print("INVALID INPUT!  Please Enter a Valid name(HINT:- only INTEGER)")
    grades[name]=grade
    
    cont = int(input("Want to continue ?\n Enter 1 for yes and 0 for no: \n"))
    stop=False
    while True:
        if cont==1:
            break
        elif cont==0:
            stop=True
            break

        else:
            print("INVALID INPUT")
    print()
    if stop==True:
        break

        
print("=============FINAL GRADES==============")

for name,grade in grades.items():
    print(f"Name of the student is {name} and Grade is {grade}")


