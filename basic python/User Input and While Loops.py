message=input("Tell me something:and i will repeat it back to you: ")
print(message)
#  The `input()` function allows you to take input from the user.
#  It waits for the user to type something and press Enter, then returns the input as
promt="if you tell us who are you, we can personalize the message you see."
promt += "\nWhat is your name? "
name = input(promt)
print(f"Hello, {name}!")

height = input("How tall are you, in inches? ")
height = int(height)  # Convert input to an integer
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older!")
    