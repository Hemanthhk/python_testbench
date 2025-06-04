#Function exercises
#Problem 1
#Given a list of integers, Return True if the sequence of numbers 1,2,3 appear in the list somewhere.

#arrayCheck([1,1,2,3,1]) -> True
#arrayCheck([1,1,2,4,1]) -> False
#arrayCheck([1,1,2,1,2,3]) ->True

def arrayCheck(nums):
    for i in range(0,len(nums)-2):  #Hopping over in steps of 3, So -2 is requried.
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

l = [1,1,2,2,1,3,1,2]
array_check_result = arrayCheck(l)
print(f"Sequence present in array passed?: {array_check_result}")

#Problem 2
#stringBits('Hello') -> 'Hlo'
#stringBits('Hi')-> 'H'
#stringBits('Heeololeo')->'Hello'

def stringBits(mystring):
    result = ""
    result = mystring[::2]  #Using slicing
    # for i in range(len(mystring)):
    #     if i%2 == 0:
    #         result = result + mystring[i]
    
    return result

even_strings = stringBits('Hello')
print(even_strings)

#Problem 3
#Given two strings, Return True is either of the strings appear at the very end, ignoring upper/lower cases (Case insensitive).
#Examples: 
#end_other('Hiabc','abc') -> True
#end_other('AbC','HiaBc') -> True

def end_other(a,b):
    a = a.lower()
    b = b.lower()

    return (b.endswith(a) or a.endswith(b))
    # return a[-len(b):] == b or b[-len(a):] ==a

result = end_other('Hiabc','aBc')
print(f"One is a substring of the other: {result}")

#Problem 4
# double_char('The')->'TThhee'

def double_char(str):
    result = ''
    for each_char in str:
        result = result + each_char*2
    return result

result = double_char('AbD')
print(result)

#Problem 5

def no_teen_sum(a,b,c):
    return fix_teen(a)+fix_teen(b)+fix_teen(c)

def fix_teen(n):
    teen = [13,14,15,16,17,18,19]
    if n in teen:
        return 0
    return n

teen_result = no_teen_sum(17,12,18)
print(f"no_teen_sum: {teen_result}")


#Problem 6
# Return even among given integers
integers = [1,2,3,4,5,6]

def even_integers(int_list):
    even_list = []
    for num in int_list:
        if num%2==0:
            even_list.append(num)
    return even_list

result_list = even_integers(integers)
print("From conventional function: {}".format(result_list))

def even_int(num):
    return num%2==0

result = filter(even_int,integers)
print(f"Using filter function: {list(result)}")

#Using lambda

result = filter(lambda num: num%2==0, integers)
print(f"Using lambda: {list(result)}")




