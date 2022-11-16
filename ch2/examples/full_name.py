first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# “To insert a variable’s value into a string, place the letter f immediately
# before the opening quotation mark. Then you can use braces to insert a variable.

## These are called 'f-strings' (format strings). They are powerful!

print(f"Hello, {full_name.title()}!")
# This prints a string and calls the 'title' method on our full_name variable in order to provide
# title case for the stored name within our string.

