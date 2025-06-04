#__name__ is used to find out if a file/module is directly run or imported from another module(file).
# Real world Application: (Refer Chatgpt Explanation in notes) Makes sure certain methods are run only when script is run directly and not when the module is imported.
#__name__ is the built-in variable which evaluates to the name of the current module.
# Example: Only if one.py is run directly from the console, __name__ will be set to "__main__". 
def func():
    print("func() in one.py")

print("TOP LEVEL ONE.PY")

if __name__ == '__main__':
    print("one.py is run directly")
else:
    print("one.py has been imported")
