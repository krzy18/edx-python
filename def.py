"""
Create a method for yourself
def hello(to="World"):
   print("Hello,", to)

name = input("What is your name? ")

hello(name)
"""

def main():
   name = input("What is your name? ")
   hello(name)

def hello(to="World"):
   print("hello,", to)


main()