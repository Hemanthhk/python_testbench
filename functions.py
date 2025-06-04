print("functions in python")


def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, I need integers!"

result = addNum("se",3)
print(result)

#Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2==0

result = filter(even_bool,mylist)
print(result) # Will return an object
print(list(result))

#Lambda expression - A breakdown of a function in a single line
#Its also called and anonymous function, Since it doesnt have a name.


lambda num: num%2==0

result_lambda = filter(lambda num: num%2==0,mylist)
print(f"Using lamba expresssion: {list(result_lambda)}")

#Useful methods

s = "hello"
s.lower()
s.upper()

tweet = "Go Sports! #Sports"
print(tweet.split('#'))
print(tweet.split('#')[1]) #Only gets whats needed

#IN OPERATOR
my_list = [1,2,3,'x']
print('x' in my_list)







