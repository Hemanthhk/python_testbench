print("control flow in Python")
#Looping thru dict
d= {"Sam":1,"Frank":2,"Dan":3}

for item in d:
    # print(f"index:{item}")
    print(f"item in dict:{d[item]}")

#Tuples
mypairs=[(1,2),(3,4),(5,6)]

for tup1,tup2 in mypairs:
    print(tup1)
    print(tup2)
#While loop
i=1
print("While loop")
while i<=5:
    print(f"i is :{i}")
    i+=1

#range - 
# A generator which generates the items with range and step specified.
# It generates the list during run time thereby saving the memory. No need to save a huge list just to iterate through it.
l=[1,2,3,4,5]
print(range(0,5))#0 is the start and 5 is the num of elements
print(list(range(0,5)))
print(list(range(0,20,2)))

for item in range(1,10):
    print(item)  #Generates number from 1 to 10. 10 excluded

#List comprehension
x = [1,2,3,4]

out = []
print("Normal for loop")
for num in x:
    out.append(num**2)
print(f"From for loop: {out}")

#List comprehension
out = [num**2 for num in x]
print(f"Using list comprehension: {out}")








