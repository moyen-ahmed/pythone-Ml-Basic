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


number = input("Enter a number, and I'll tell you if it's even or odd: ")
if int(number) % 2==0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")#  a string.
#  The `input()` function can also take a prompt string to display to the user.     

#While loop structure
#  A while loop continues to execute as long as a condition is true.
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1  # Increment the number by 1 each time through the loop 

promt = "\nTell me something, and I will repeat it back to you."
promt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(promt)
    if message != 'quit':
        print(message)