

#ask the user their name
userName = input("what is your name? ")
#age
userAge = input("how old are you? ")
#make answer int
userAgeint = int(userAge)

print("hello there " + userName)

userAgeTenTime = userAgeint * 10
print("your age ten times is " + str(userAgeTenTime))


if (userAgeint >= 18):
    print("you are old enough to vote!")
else:
    print("you are not old enought to vote!")
