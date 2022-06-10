#!/usr/bin/env python3

print("Select operation")
print("\t1. Add")
print("\t2. Subtract")
print("\t3. Multiply")
print("\t4. Divide")

userChoice = int(input("Enter your choice (1/2/3/4): "))
userInput1 = float(input("Enter first number: "))
userInput2 = float(input("Enter second number: "))

if userChoice == 1:
    addResult = int(userInput1 + userInput2)
    print(int(userInput1),"+",int(userInput2),"=",addResult)
elif userChoice == 2:
    subResult = int(userInput1 - userInput2)
    print(int(userInput1),"-",int(userInput2),"=",subResult)
elif userChoice == 3:
    multResult = int(userInput1 * userInput2)
    print(int(userInput1),"*",int(userInput2),"=",multResult)
elif userChoice == 4:
    divResult = userInput1 / userInput2
    print(int(userInput1),"/",int(userInput2),"=",divResult)
