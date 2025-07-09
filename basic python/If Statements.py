#if Statements are fundamental control structures in Python that allow you to execute code conditionally based on whether a certain condition

car=["BMW", "Mercedes", "Audi"]
for c in car:
    if c == "BMW":
        print("This is a BMW")
    elif c == "Mercedes":
        print("This is a Mercedes")
    else:
        print("This is an Audi")
        
best_player="Ronaldo is the best player in the world"
 
answer=13
if answer != 42:
    print("The answer is not 42")
    
 #in is a membership operator that checks if a value exists in a sequence (like a list, tuple, or string).

requested_food=["pizza", "burger", "pasta"]
print("pizza" in requested_food)  # True
print("salad" in requested_food)  # False is true or false. 

banned_users=["Alice", "Bob", "Charlie"]
user="David"
if user not in banned_users:
    print(f"{user} is allowed to post a response.") 
    
      
#if statements can be nested, meaning you can place one if statement inside another. This allows for more complex decision-making.
age = 20    
if age >= 18:
    print("You are an adult.")
    if age >= 21:
        print("You can drink alcohol.")
    else:
        print("You cannot drink alcohol yet.")      
        
#elif statements allow you to check multiple conditions in a sequence. If the first condition is false, it checks the next one.
age = 16
if age < 13:  
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")    
else:
    print("You are an adult.")
        
         