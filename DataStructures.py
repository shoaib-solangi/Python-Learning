print("alhamdulillah data structures prhy ga ")


# WHAT ARE DATA STRUCTURES IN PYTHON?
# Data structures in Python are specialized formats for organizing, processing, and storing data. They allow for efficient data manipulation and retrieval. Common data structures include:
# 1. Lists: Ordered collections of items that can be changed.       
# 2. Tuples: Ordered collections of items that cannot be changed.
# 3. Sets: Unordered collections of unique items.
# 4. Dictionaries: Collections of key-value pairs that allow for fast data retrieval.






# Lists


# list methods


# numbers = [1 , 2 ,3,4,5,6]
# numbers.append(10)
# numbers.insert(3 , 14)
# numbers.extend([100,155,54])
# numbers.remove(14)
# numbers.sort()
# print(numbers)


# num = [0 ,-1,-2,-3,5,6,7,9]
# positiveNum = []
# negativeNum = []
# for i in range(len(num)):
#     if num[i] > 0:
#         positiveNum.append(num[i])
#     elif num[i] == 0:
#         print("this is zero")
#     else:
#         negativeNum.append(num[i])
    
# print(f"positive Numbers are : {positiveNum}" )
# print(f"Negative Number are : {negativeNum}")


# question - 2 
# mean  = [1 ,2,3,34,5,64,86]

# solved = 0
# for i in mean:
#     solved += i
# print(f"Sum of the list is : {solved}")
# solvedAns = solved / len(mean)
# print(f"Mean of the list is : {solvedAns}")

# question - 3
l = [ 1,2,3,4,5,6,7,8,9,10]
largest = l[0]
index =0
secondLargest = l[0]
secondIndex = 0
for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i
    

print(f"Largest number in the list is : {largest} at index {index}")     
for i in range(len(l)):
    if l[i] > secondLargest and l[i] != largest:
        secondLargest = l[i]
        secondIndex = i

print(f"{secondLargest} at index {secondIndex}")



lengt = [1 ,2,3,4,5,6,7,8,9,10]
num = 0

for i in range(len(lengt)-1):
   
    if lengt[i] > lengt[i+1]:
        continue
    
    else:
        print("false")
        break
else:
    print("true")










# Tuples

a = (1, 2, 3, 4, 5 )
# we cannot change the values of a tuple
# a[0] = 10  # This will raise an error
# Tuples are immutable, meaning they cannot be changed after creation.
print(type(a))

print(a.index(3))
print(a.count(2))


# tuple Unpacking
x, y, z = (1, 2, 3)
print(f"x: {x}, y: {y}, z: {z}")

a = (1)
print(type(a))  # This will print <class 'int'> because it's not a tuple
a = (1,)  # This is a tuple with one element    





# Sets
# A set is an unordered collection of unique items.
s = {1, 2, 3, 4, 5}
# set is based on hash 

s.add(6)
s.remove(3)
s.discard(2)  # Does not raise an error if 2 is not present
pop  = s.pop()  # Removes and returns an arbitrary element
print(f"Set after operations: {s}")


# Dictionry
a = {} # this is an empty dictionary

b = {"name": "Ali", "age": 25, "city": "Karachi"}
print(b["city"])

for i in b:
    print(i , ':' , b[i])



# deep copy and shallow copy 
# deep copy creates a new object and recursively adds copies of nested objects found in the original.
# shallow copy creates a new object but inserts references into it to the objects found in the original
a=  [ 1,2,3,4]
# deep copy
b = a
b[0] = 100
print(a)


c = a.copy()  # This is a shallow copy
c[0] = 200
print(a)  # This will still print [100, 2, 3, 4] because b is a reference to a



# IN dictionart

d = {1: 100}
d2 = d.get(1)
print(d2)


#help(dict)

# dictionary methods
# d = {"name": "Ali", "age": 25, "city": "Karachi"}
# d["country"] = "Pakistan"  # Adding a new key-value pair  
# 

# question - 1 
d1 = {10: 411 , 20: 25}
d2 = {30: 100, 40: 200}


for i in d2:
    d1[i] = d2[i]  # Merging d2 into d1

print(d1)  # This will print {10: 411, 20: 25, 30: 100, 40: 200}

# question - 2

d3 = {1 : 100 , 2 : 200 , 3 : 300}
sum = 0
for i in d3:
    sum += d3[i]

print(f"Sum of the values in the dictionary is : {sum}")  # This will print 600



# question - 3

aa = [1,1,1,12,1,1,2,2,2,2,3,3,3,4,4,5] # check frequency
dict = {}
for i in aa:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1
    
        
print(f"Frequency of  all elements in the dictionary  is : {dict}")  # This will



# question - 4

d4 = {1: 100, 2: 200, 3: 300}
d5 = {3: 400, 5: 500}

for i in d5:
    if i in d5.keys():
        d4[i] = d5[i]  # Updating the value if the key exists
    else:
        d4[i] = d5[i]
print(f"Updated dictionary after merging d5 into d4: {d4}")  # This will print {1: 100, 2: 200, 3: 400, 5: 500}