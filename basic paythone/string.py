name="ishtiak ahmed moyen"
print(name.title())
# This will print the name with the first letter of each word capitalized.
print(name.upper())
# This will print the name in uppercase.
print(name.lower()) 
# This will print the name in lowercase.
first_name= "ishtiak"
last_name= "moyen"
print(f"Hello, {first_name} {last_name} welcome to the world of python")
# This will print a formatted string with the first and last name. 
# The f-string allows you to embed expressions inside string literals, using curly braces `{}`.

# rstrip
# This method is used to remove trailing whitespace from a string.
# For example, if you have a string with extra spaces at the end, you can use
favorite_language = "python "
print(favorite_language.rstrip())
# This will remove any trailing whitespace from the string.

# lstrip
# This method is used to remove leading whitespace from a string.   
favorite_language = " python"
print(favorite_language.lstrip())

# strip
# This method is used to remove both leading and trailing whitespace from a string. 
favorite_language = " python "
print(favorite_language.strip())
favorite_language=favorite_language.strip()
print(favorite_language)