#Find the positive integer that is divisible by both 11 and 12
"""
It is sometimes convenient to exit a loop without testing the loop condition. Executing a break
statement terminates the loop in which it is contained, and transfers control to the code immediately
following the loop.
"""
x = 1
while True:
    if x%11 == 0 and x%12 == 0:
        break
    x = x + 1
print(x, 'is divisible by 11 and 12')
