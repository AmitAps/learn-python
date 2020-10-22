"""
Write a program that asks the user to input 10 integers, and then prints the largest
odd number that was entered. If no odd number was entered, it should print a message to that effect.
"""

intNum = 0
largestNum = 0
while(intNum != 10):
    x = int(input('Enter 10 integer: '))
    intNum = intNum + 1
    if x > largestNum:
        if x%2 != 0:
            largestNum = x
if largestNum != 0:
    print("Largest odd number you have entered is: ",largestNum)
else:
    print("You haven't entered any odd Numbers.")



