"""
#this is for integer
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x+y)

"""

"""
#this is for float
x = float(input("First number: "))
y = float(input("Second number: "))

#rounding numbers
z = round(x+y)

#print the total with comma(e.g. 1,000)
print(f"Total: {z:,}")"""

"""

x = float(input("First number: "))
y = float(input("Second number: "))

z = x / y

#print the total with round-off(e.g. :.2f)
print(f"Total: {z:.2f}")"""

def main():
    x = int(input("What is first number: "))
    print("x squared is", squared(x))

def squared(n):
    return n * n

main()