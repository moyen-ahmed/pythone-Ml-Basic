aline_0={'color':'red','fruit':'apple','pet':'dog','age':7}
print(aline_0['color'])
print(aline_0['fruit'])
print(aline_0['pet'])

aline_0 = {}
aline_0['color'] = 'red'
aline_0['fruit'] = 'apple'  
aline_0['pet'] = 'dog'
aline_0['age'] = 7
print(aline_0)


# Adding a new key-value pairaline_0['city'] = 'New York'
print(aline_0)  
# Removing a key-value pair
del aline_0['age']
print(aline_0)
# Checking if a key exists
if 'color' in aline_0:
    print("Key 'color' exists in the dictionary.")  
else:
    print("Key 'color' does not exist in the dictionary.")

favourite_languages = {
    'alice': 'python',
    'bob': 'java',
    'charlie': 'c++',
    'dave': 'javascript'
}
languages=favourite_languages['bob'].title()
print(f"{languages} is Bob's favourite language.")
# Iterating through a dictionary
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")    
# Iterating through keys
for name in favourite_languages.keys():
    print(name.title()) 
    

#Looping through the  dictionary

user_0 = {
    'username': 'john_doe', 
    'first': 'John',
    'last': 'Doe',
    'location': 'New York',
    'age': 30
}
for attribute, info in user_0.items():
    print(f"{attribute.title()}: {info}")
    
#Nesting dictionaries
users = {
    'user1': {
        'username': 'alice',
        'first': 'Alice',
        'last': 'Smith'
    },
    'user2': {  
        'username': 'bob',
        'first': 'Bob',
        'last': 'Johnson'
    }       
}
for user, details in users.items():
    print(f"\nUsername: {user}")
    for attribute, value in details.items():
        print(f"{attribute.title()}: {value}")
        
aline_0 = {'color': 'red', 'fruit': 'apple', 'pet': 'dog', 'age': 7}
aline_1 = {'city': 'New York', 'country': 'USA'}
aline_2 = {'hobby': 'reading', 'sport': 'soccer'}
alines = [aline_0, aline_1, aline_2]
for aline in alines:
        print(aline)