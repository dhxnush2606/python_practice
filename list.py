# a=[1,2,3,4,5]
# b=a
# b.append(6)
# print(a)
# print(b)

# letter=list("python")
# print(letter)

#string slicing 

# a=['dhanush',18,'bca',34.34,'3rdsem']
# # b=a[::]
# # print(b)
# # a.remove(18)
# a[1]=20
# print(a)

#nested list 

# l1=['hello',['dhanush',18,'siuu'],'world','vanniyar']
# print(l1[1])

#problem solving

#1) create a list of your 5 favourite programming languages. Print the first and the
# last one using both positive and negative indexing.

# a=['messi','ronaldo','mbappe','lamine','pedri']
# print(a[0::4])
# print(a[-5::4])

# problem 2
# Slice the Marks
# Given marks = [45, 67, 89, 23, 90, 56, 78] :
# Print the first 3 marks
# Print the last 2 marks
# Print every alternate mark
# Print the list in reverse

# marks=[45,67,89,23,90,56,78]
# print(marks[0:3])
# print(marks[-1:-3:-1])
# print(marks[0::2])
# print(marks[::-1])

# PROBLEM 3
# Todo List Manager
# Start with todos = ["wake up", "study"] . Then:
# Add "exercise" at the end
# Add "meditate" at the very beginning
# Remove "study"
# Replace the last item with "sleep"
# Print the final list

# todos = ['wake up','study']
# todos.append('exerxise')
# todos.insert(0,'mediate')
# todos.remove('study')
# todos[-1]='sleep'
# print(todos)

# PROBLEM 4
# Student Record (Nested)
# Create a nested list where each inner list is [name, marks] for 3 students. Print
# the name of the 2nd student and the marks of the 3rd student.

# result=[['dhanush',99],['messi',50],['ronaldo',100]]
# print(result[1][0],result[2][1])

# #problem 5
# Unpack the Coordinates
# You have data = [101, "Varanasi", 25.3, 82.9] = id, city, lat, lon. Unpack it
# into four named variables in a single line and print a sentence using them.

# data=[101,'varanasi',25.3,82.9]
# id,city,lat,lon=data
# print(f"id={id},city={city},lat={lat},lon={lon}")

# PROBLEM 6
# The Copy Trap
# Create original = [1, 2, 3] . Make a copy called backup . Append 99 to
# backup . Print both lists and explain (in a comment) why original did NOT
# change. Then deliberately create the bug using = and observe the difference

a=[1,2,3]
b=a
b.append(99)
print(a) #here a also changed 

c=[1,2,3]
d=c.copy()
d.append(99)
print(d,c)

