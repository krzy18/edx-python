"""
#Operations
def main():
    firstNumber = int(input("What will be your first number? "))
    secondNumber = int(input("And your second number? "))
    print(f"Addition: {firstNumber + secondNumber}\nSubtraction: {firstNumber - secondNumber}\nProduct: {firstNumber * secondNumber}\nDivison: {firstNumber / secondNumber}\nPower of: {firstNumber ** secondNumber}\nRemainder: {firstNumber % secondNumber}\nGreater Than?: {firstNumber > secondNumber}\nLess Than?: {firstNumber < secondNumber}\nEqual To?: {firstNumber == secondNumber}")


main()
"""

"""def main():
    storage = ["John", "Keith", "Jerome"]
    print(f"These are the names of the people {storage[0]}")

main()

Student = {"Name": "Ryan", "Age": 23, "Course": "Biotlogy"}

print(Student["Age"])"""

"""def myFunction():
    storage = ["John", "Keith", "Jerome"]
    print(f"These are the names of the people: {storage[0:2]}")

    Student = {"Name": "Ryan", "Age": 23, "Course": "Biotlogy"}

    print(Student["Age"])

myFunction()"""


"""#If Elif Statement

def main():
    firstnum = int(input("What is the first number: "))
    secondnum = int(input("What is the second number: "))
    operation = input("What operation do you want to use? (e.g +, -, *, /): ")

    math(firstnum, secondnum, operation)

def math(x, y, z):
    if z == "+":
        print(f"Total: {x+y}")
    elif z == "-":
        print(f"Total: {x-y}")
    elif z == "*":
        print(f"Total: {x*y}")
    elif z == "/":
        print(f"Total: {x/y}")
    else:
        print("You forgot to put operation")


main()"""

"""#For Loops

for i in range(6):
    print("*" * i)"""

"""#While Loops
def main():
    myNum = int(input("What is the number: "))
    
    while myNum < 10:
        print(f"{myNum} is less than 10")
        myNum += 1

main()"""

if 5 * 2 == 11 or 10 * 2 == 21:
    print("Success")
