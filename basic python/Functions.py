# def greet_user(username):
#     print(f"Hello, welcome to the Python programming world!,{username.tittle()}!")    
# greet_user("Alice,habibi")

def greet_user(username):
    print(f"Hello, welcome to the Python programming world!, {username.title()}!")    

greet_user("Alice,habibi")

#Passing arguments
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
