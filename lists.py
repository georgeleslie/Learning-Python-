

student1 = "George"
student1age = 33
student1gpa = 3.48

student2 = ""

studentNames = ["George", "Ell", "Scott", "Darren"]

print(studentNames)

print(studentNames[2])

for name in studentNames:
    print(name)


studentNames.append("Joe")

for name in studentNames:
    print(name)

studentNames.remove("Darren")

for name in studentNames:
    print(name)



#tuples are unchangeable you can index
studentTuple = ("Tom", "Dick", "Harry")
print(studentTuple)


#sets you cant even index and they are not ordered. you can loop through them both though