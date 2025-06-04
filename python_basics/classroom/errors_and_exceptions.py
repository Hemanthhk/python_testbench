print("Module: Errors and exceptions in Python")


try:
    f = open('simple.txt','r')
    f.write("Test write to simple text!")

# except IOError:
#     print("Error: While writing data to the file")
except Exception:
    print("Error occured!")


else: #This will execute if there are no exceptions
    print("SUCCESS!")
    f.close()

finally: # This will work no matter what
    print("I ALWAYS WORK NO MATTER WHAT!")
