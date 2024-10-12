

studentGrades = {"George": 92, "Danny": 62, "Jimmy": 222}

print(studentGrades["George"])

myCars = ({"Make": "Ford", "Model": "Model A", "Model": "Model B", "Year": 2031},
        {"Make": "Lamboghini", "Model": "Aventador", "Year": 2026})


print(myCars[1]["Model"])


for item in studentGrades:
    print(item)
    print(studentGrades[item])


#this doesnt work
#if 92 in studentGrades:
    #print("It is!")

if 92 in studentGrades.values():
    print("It is!")

#this prints all values
print(studentGrades.values())

#this converts dictionary in to list
values = studentGrades.values()
valuesList = list( values )
print(valuesList[1])

keys = studentGrades.keys()
keysList = list( keys )
print(keysList)

#combine and iterate through the dictionaries
for i in range(0,len(values)):
    print(studentGrades[keysList[i]])

#way to single out in dictionaries
items = studentGrades.items()
print(items)
itemslist = list( items)
print(itemslist[0][1])


