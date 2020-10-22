lastNum = 50
primeNumber = ''
itersLeft = lastNum
for pNum in range(1, lastNum):
    if pNum%1 == 0 and pNum%(pNum+1) == 0:
        primeNumber = primeNumber + str(pNum)
print(primeNumber)
