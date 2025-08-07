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

#Returning a value
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# whle True:
def get_formatted_name(first_name, last_name,):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    f_name= input("First name: ")
    l_name= input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    
#passing  a list
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

user_names = ['hannah', 'ty', 'margot']
greet_users(user_names) 


#Example unprinted designs
# This code simulates a 3D printing process where designs are printed one by one from a list of unprinted designs. Each design is printed and then moved to a list of completed models. Finally, it prints out all the completed models.

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}.")
    completed_models.append(current_design) 
    
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    #passing arbitary number of arguments
    