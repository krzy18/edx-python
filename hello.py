"""
# comment - Ask user to input their name and Remove whitespace from string and capitalize
myName = input("What's your name? ").strip().title()


#split users name into first name and last name

first, last = myName.split(" ")

#Print Hello to user
print(f"Hello, {first}")

#Say hello to user
#print("hello, \"friend\"")
# """