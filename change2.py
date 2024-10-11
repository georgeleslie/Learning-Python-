



changeamount = input("What is the customers change amount? ")
changeamount = int(changeamount) #converting to int

numFiftyp = changeamount // 50 #figure out number of quaters
changeamount = changeamount - (numFiftyp * 50)

numTwentyp = changeamount // 20 #figure out number of dimes
changeamount -= (numTwentyp * 20)

numTenp = changeamount // 10 #figure out number of nikles
changeamount -= (numTenp * 10)

numFivep = changeamount // 5 #figure out number of pennies
changeamount -= (numFivep * 5)

print("Fiftys: ", numFiftyp)
print("Twentys: %s" % numTwentyp)
print("Tens: {}" .format(numTenp))
print(f"Fives: {numFivep}")
print("Final change amount: " + str(changeamount))