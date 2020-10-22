numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
itersLeft = numXs
while(itersLeft != 0):
    toPrint = toPrint + str(numXs)
    itersLeft = itersLeft - 1
print(toPrint)
