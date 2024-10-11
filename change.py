


changeamount = 2333

numFiftyp = changeamount // 50 #figure out number of quaters
changeamount = changeamount - (numFiftyp * 50)

numTwentyp = changeamount // 20 #figure out number of dimes
changeamount -= (numTwentyp * 20)

numTenp = changeamount // 10 #figure out number of nikles
changeamount -= (numTenp * 10)

numFivep = changeamount // 5 #figure out number of pennies
changeamount -= (numFivep * 5)

print("Fiftys: " + str(numFiftyp))
print("Twentys: " + str(numTwentyp))
print("Tens: " + str(numTenp))
print("Fives: " + str(numFivep))

print("Final change amount: " + str(changeamount))