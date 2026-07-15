# Docstring -- A docstring (documentation string) is a string written immediately after a function, class, or module definition to explain what it does.
# It is enclosed in triple quotes (""" """ or ''' ''').
# comments are ignored by python but the doctstring is stored as an attribute of the function, class, or module and can be accessed using the __doc__ attribute or the help() function.

def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

print(greet("Ayaan")) 
print(greet.__doc__)
help(greet)

# Best Practices for Function Design
# Use snake_case for function names (calculate_salary).
# Give functions one clear responsibility.
# Keep functions small and focused.
# Write a docstring for every public function.
# Prefer return over print.
# Avoid modifying global variables when possible.
# Use descriptive parameter names (price, quantity) instead of generic ones (x, y).