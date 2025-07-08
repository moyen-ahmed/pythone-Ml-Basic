bicycle=['mountain bike', 'road bike', 'hybrid bike', 'cruiser bike']
print(bicycle[0])
# Accessing the first element of the list
print(bicycle[1]
)# Accessing the second element of the list
print(bicycle[2])
# Accessing the third element of the list
print(bicycle[3])
# Accessing the fourth element of the list     
print(bicycle[-1])
# Accessing the last element of the list

#Now Changuing,Adding and Removing elements from the list

motorcycle=['harley', 'ducati', 'yamaha', 'honda']
print(motorcycle)

motorcycle[0]='suzuki'# Changing the first element
print(motorcycle)

#append() method to add an element to the end of the list

motorcycl=[]
motorcycl.append('suzuki')
motorcycl.append('harley')  
motorcycl.append('ducati')
motorcycl.append('yamaha')
print(motorcycl)

#insert() method to add an element at a specific position
motorcycl.insert(0, 'honda')  # Adding 'honda' at the beginning
print(motorcycl)
motorcycl.insert(2, 'kawasaki')  # Adding 'kawasaki' at index 2
print(motorcycl)

#delete an element from the list using del statement
del motorcycl[1]  # Deleting the second element
print(motorcycl)

#pop() method to remove the last element from the list
last_motorcycle = motorcycl.pop()  # Removes and returns the last element
print(last_motorcycle)  # Output: 'yamaha'
print(motorcycl)  # Remaining list after pop

#remove() method to remove a specific element from the list
motorcycl.remove('kawasaki')  # Removes 'kawasaki' from the list        
print(motorcycl)  # Remaining list after remove

#sort() method to sort the list in alphabetical order
motorcycl.sort()  # Sorts the list in ascending order
print(motorcycl)  # Output: ['ducati', 'harley', 'honda', 'suzuki']

alpphabet=['zebra', 'apple', 'orange', 'banana']
alpphabet.sort()  # Sorts the list in alphabetical order
print(alpphabet)

#reverse() method to reverse the order of the list
alpphabet.reverse()  # Reverses the order of the list
print(alpphabet)

#len() function to get the number of elements in the list
print(len(alpphabet))  # Output: 4 (number of elements in the list)

# Using a for loop to iterate through the list
football_teams = ['Barcelona', 'Real Madrid', 'Manchester United', 'Bayern Munich']
# Iterating through the list of football teams
# team=store the current team in the loop
for team in football_teams:
    # Print each team in the list
    print(team)
    print(f"{team} is a great team!")  
    # Print a message for each team
    print(f"There are {len(football_teams)} teams in the list.") 
# Print the total number of teams in the list
print(f"There are {len(football_teams)} teams in the list.")

#Numerical lists
for value in range(1, 6):
    # Print numbers from 1 to 5 
    print(value)
    
# Using range() to create a list of numbers
numbers = list(range(1, 11))  # Creates a list of numbers from 1 to 10
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   

# Using range() to create a list of even numbers
even_numbers = list(range(2, 21, 2))  # Creates a list of even numbers from 2 to 20
#here 2 is the start, 21 is the stop (exclusive), and 2 is the step
print(even_numbers)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 

# Using range() to create a list of odd numbers
odd_numbers = list(range(1, 21, 2))  # Creates a list       
#here 1 is the start, 21 is the stop (exclusive), and 2 is the step
print(odd_numbers)  # Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

3# Using range() to create a list of squares
squares = []    
for value in range(1, 11):  # Looping through numbers from 1 to 10
    square = value ** 2  # Calculating the square of each number
    squares.append(square)  # Appending the square to the list      
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Using list comprehension to create a list of squares
squares_comprehension = [value ** 2 for value in range(1, 11)]  # Creates a list of squares from 1 to 10
print(squares_comprehension)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Using min() and max() functions to find the minimum and maximum values in a list
min_value = min(squares)  # Finds the minimum value in the list of squares      
max_value = max(squares)  # Finds the maximum value in the list of squares
print(f"Minimum value: {min_value}")  # Output: Minimum value: 1    
print(f"Maximum value: {max_value}")  # Output: Maximum value: 100
# Using sum() function to calculate the sum of all elements in a list
total_sum = sum(squares)  # Calculates the sum of all squares in the list
print(f"Total sum of squares: {total_sum}")  # Output: Total sum of squares: 385

players = ['Messi', 'Ronaldo', 'Neymar', 'Mbappe']
print(players[0:2])  # Output: ['Messi', 'Ronaldo'] (slicing the first two elements)
print(players[1:3])  # Output: ['Ronaldo', 'Neymar'] (slicing the second and third elements)
print(players[:3])   # Output: ['Messi', 'Ronaldo', 'Neymar'] (slicing the first three elements)
print(players[2:])   # Output: ['Neymar', 'Mbappe'] # Output: ['Neymar', 'Mbappe'] (slicing from the third element to the end)
print(players[-2:])  # Output: ['Neymar', 'Mbappe'] # Slicing the last two elements
print(players[-3:-1])  # Output: ['Ronaldo', 'Ney   mar'] # Slicing from the third last to the second last element
print(players[-3:])  # Output: ['Ronaldo', 'Neymar', 'Mbappe'] # Slicing from the third last element to the end 

#Tuples
# Tuples are immutable lists, meaning they cannot be changed after creation
dimensions = (1920, 1080)  # Creating a tuple with two elements
print(dimensions)  # Output: (1920, 1080)
print(dimensions[0])  # Accessing the first element of the tuple
print(dimensions[1])  # Accessing the second element of the tuple   
