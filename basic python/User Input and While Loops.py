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
message = ""#  Initialize an empty string for the message
#  The `input()` function can be used to get user input in a loop.
while message != 'quit':
    #  The loop continues until the user types 'quit'.
    message = input(promt)
    if message != 'quit':
        print(message)
        
 #Example 2
current_number = 0
while current_number < 10:
    current_number += 1  # Increment the number by 1 each time through the loop
    if current_number % 2 == 0:  # Check if the number is even
        continue  # Skip the rest of the loop for even numbers
    print(current_number)  # Print only odd numbers
            
            
            
            
            
#while loop with list and dictionary
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # Remove the last user from the list
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)  # Add the user to the confirmed list
    
    print(f"Confirmed users: {confirmed_users}")
#  This code demonstrates how to take user input and use while loops in Python.
    for user in confirmed_users:
        print(f"User {user.title()} has been confirmed.")
        
        
#Example 3: Removing all instances of a specific value from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'dog']
print("Original list of pets:", pets)
#  This code demonstrates how to take user input and use while loops in Python.
#  The `pop()` method removes the last item from a list and returns it.
while 'dog' in pets:    
    pets.remove('dog')  # Remove the first occurrence of 'dog' from the list
print("Updated list of pets:", pets)

        
# Example 4: Filling a dictionary with user input
responses = {}
#  This code demonstrates how to take user input and use while loops in Python.
polling_active = True
while polling_active:   
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the response in the dictionary
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False  # End the polling
        
# Display the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
           