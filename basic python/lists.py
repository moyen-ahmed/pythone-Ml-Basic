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

#Num