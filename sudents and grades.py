grades={}

continue_loop=True
print("================Student and Grades================")
while continue_loop:
    is_valid= False
    while not is_valid:
        first_name=input("Enter The First Name Of The Student: \n").strip()
        last_name=input("Enter The Last Name Of The Student: \n").strip()
        if first_name.isalpha() and (last_name.isalpha() or last_name == ""):
             is_valid=True
             name=first_name+" "+last_name
        else:
            print("INVALID INPUT! Please Enter a Valid name(HINT:- only ALPHABETS)")
    is_valid=False
    while not is_valid:
        grade=input("Enter The Grade Of The Student: \n")
        if grade.isnumeric() and 0<=int(grade)<=100:
            is_valid=True
        else:
            print("INVALID INPUT!  Please Enter a Valid name(HINT:- only ALPHABETS)")
    cont = int(input("Want to continue ?\n Enter 1 for yes and 0 for no: \n"))
    valid=False
    while not valid:
        if cont==1:
            valid=True
        elif cont==0:
            valid=True
            continue_loop=False
        else:
            print("INVALID INPUT")
        
    grades[name]=grade
print("=============FINAL GRADES==============")
for name,grade in grades.items():
    print(f"Name of the student is {name} and Grade is {grade}")




    