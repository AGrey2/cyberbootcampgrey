## Write a multi-line comment with your name, favorite food, and dream job on 3 different lines.
'''
My name is Alexis.
My fav food is Shrimp Tacos.
My dream job is Cyber Analyst

'''

# assign 5 different data types to 5 different variables. At least one datatype must be a string.
integer=15
float=68.7
string = "Alexis Grey"
boolean=True
list=[1,2,3,4,5]

# print the length of your string.
print (len(name))

# create a new variable called savvy, and assign it the string with this phrase "Learning Python is Awesome!"
savvy = "learning Python is awesome"


# Replace "Awesome" with "great" in the string

new_savvy = savvy.replace("Awesome", "great")

# Create and assign 3 more variables called name, age and length using the multi-variable naming method.
name, age, length = "Alexis", 29, 63


# Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today."


miniBio=(f"Hi my name is {name}, I am {length}, and I am {age} old today")
print(miniBio)


# Create a list of at least 5 elements of mixed data types
list=[6, "python",{"Alexis":29}, 3.14]

# replace a part of it with something else
list[2]="age"
print(list)
# append or insert several more items to the list
list.append(23)
list.insert(1, True)

# find and print the length of the list
print(len(list1))
# slice a sub-section of the 1st list, and save it to a different 2nd list
list2=list1[1:2]
# print the 2nd list
print(list2)
# extend your original list with the 2nd list sliced above
list1=list2[1:2]
# Create a new list called "simList" containing at least 5 elements of the same data type, either string, integer, float, or Boolean.
simList=[1,71,1,23,42]
# sort "simList", and print the list
simList.sort()
print(simList)
# copy the "simList" list to another 3rd list
list3=simList.copy()
# add the 2nd and 3rd lists together into a 4th list
list4=list2 + list3
print(list4)

