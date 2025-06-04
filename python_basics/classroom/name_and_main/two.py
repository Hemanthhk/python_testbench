#__name__ is used to find out if a file/module is directly run or imported from another module(file)
#__name__ is the built-in variable which evaluates to the name of the current module.
# Example: Only if one.py is run directly from the console, __name__ will be set to "__main__".

import one  #When you import a module (file), Python will Execute everything outside the methods. 
#In this case everything outside of func() in one.py

print("TOP LEVEL TWO.PY")

one.func()

if __name__ =='__main__':
    print("two.py is run directly")
else:
    print("two.py has been imported")
