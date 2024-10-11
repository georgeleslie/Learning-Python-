

name = "George"
age = 33

print("Hello my name is " + name + ", I am " + str(age) + " years old")

print("Hello my name is %s, I am %s years old." % (name, age))

print("Hello my name is {0}, I am {1} years old." .format(name, age))

print(f"Hello my name is {name}, I am {age - 10} years old.")

message = (
    f"Hello {name}. "
    f"You are {age} years old, "
    f"in ten years you will be {age + 10} years old."
)

print(message)




