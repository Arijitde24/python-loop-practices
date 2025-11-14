my_dictionary={"A":45,"B":30}
print(my_dictionary)
print(my_dictionary["A"])
my_dictionary["C"]=78
print(my_dictionary)
my_dictionary["A"]=40
print(my_dictionary)
del my_dictionary["B"]
print(my_dictionary)

grades={"Nora":86,"Gino":55}
print(len(grades))
grades["Alexander"]=34
print(grades)
grades["Gino"]=78
print(grades)
print(grades.keys())
print(grades.values())
print(grades.items())
grades.update({"Nora":26,"Jack":19})
print(grades)


nest_dictionary = {
    "Nora": {
        "age": 15,
        "weight": 67,
        "height": 158
    },
    "Gino": {
        "age": 17,
        "weight": 80,
        "height": 160
    }
}
print(nest_dictionary)
print(nest_dictionary["Nora"]["age"])
nest_dictionary["Nora"]["age"] = 16
print(nest_dictionary)