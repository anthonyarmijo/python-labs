# Stripping whitespace can be a useful tool for data validation
# e.g. taking user input for their username
# In these cases, you would sometimes want to ignore any excess whitespace entered by the user

# Ensure no whitespace exists at right side of string, using the rstrip() method
favorite_language = 'python '
favorite_language
'python '

favorite_language.rstrip()
favorite_language
'python'

# permanently remove whitespace
favorite_language = favorite_language.rstrip()

# strip from leftside:
favorite_language = " python "
favorite_language.lstrip()

# strip both sides
favorite_language = " python "
favorite_language.strip()