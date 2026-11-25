# # tuple
# t1= ()
# print(type(t1))

# tuple is immutable
# l1 =(34,55,45)
# l1[0]=45
# print(l1)

# # tuple packing

# t2=12,13,"dhanush","vanniyar"
# print(type(t2),t2)

# # tuple unpacking
# a,b,*name=t2
# print(a,b,name)

# set is an unordered collection of unique items 

# s1 ={5,10,23,10,5,4,4,3}
# print(type(s1),s1)

# s2={1,2,3,4,5,}
# print(s2)

# # add and remove and discard function 
# s3={1,2,3}
# s3.add(4)
# # s3.remove(5) # here if the item is not found then it will show error 
# s3.discard(5)  #here no error will be shown if if the the item is not found 
# print(s3)

# set operation
# s5 = {1,2,3,4,5,8}
# s6 = {1,2,3,4,5,6,7}
# new_set1 = s5 | s6
# new_set2 = s5 & s6
# new_set3 = s5 - s6
# new_set4 = s5 ^ s6
# print(f"{new_set1},{new_set2},{new_set3},{new_set4}")

# frozenset
 
# fs = frozenset({1,2,3,4,5})
# print(fs)
# fs.add(6)


# key difference between set and list is time 

# big_list = [1,2,3,4,..., 999999] 
# big_set = {1,2,3,4,..., 999999}

# a = 999999 in big_list # slow - checks the item one by one (0(n))
# b = 999999 in big_set # fast - jumps straight ot it (0(1))


# ------------------------------------------------------------

# # Common Friends
# Two people's friend lists: a = {"Ravi", "Sara", "Deep", "Amit"} and b =
# {"Sara", "Amit", "Neha"} . Print their common friends and all friends combined

# a = {"Ravi","Sara","Deep","Amit"}
# b = {"Sara","Amit","Neha"}

# c= a & b 
# d = a | b 

# print(f"common friend : {c} all combined friend : {d}")

# ----------------------------------------------------------------

# Swap Without a Temp Variable
# Take two numbers from the user and swap their values using tuple unpacking (no
# # third variable). Print before and after.

# a = tuple(input("enter a number : "))
# b = tuple(input("enter another number  : "))
# print (f"before a = {a} and b = {b}")
# a,b = b,a 
# # b = a

# print (f"after a= {a} and b= {b} ")

# ---------------------------------------------------------------

# HOMEWORK 3
# Unique Words Counter
# Take a sentence from the user. Split it into words and print how many unique
# words it contains (ignore repeats)

# a = str(input(" enter a sentence : "))

# a.split()
# a = set(a)
# b=len(a)

# print(f"splited into words : {a} \n unique words : {b}")

# ----------------------------------------------------------------

# Who Dropped Out?
# registered = {"A", "B", "C", "D", "E"} signed up, but attended = {"A", "C",
# # "E"} showed up. Use set difference to find who did NOT attend

# registered = {"A","B","C","D","E"}
# attended = {"A","C","E"}

# dropped_out = registered - attended

# print(dropped_out)

# ---------------------------------------------------------------

# # namedtuple

# from collections import namedtuple

# employee = namedtuple('employee',['id','name','salary'])

# l1 = [4,'messi',1000000]
# l2 = [5,'ronaldo',200000]

# s1 = employee(1,"dhanush",50000)
# s2 = employee(2,"rahul",60000)
# s3 = employee(3,"rajesh",70000)
# s4 = employee._make(l1)
# s5 = employee._make(l2)

# d1 = s1._asdict()

# new_s1 = s1._replace(salary=200000)

# print(s1)
# print(s4)
# print(d1)
# print(new_s1)

# ------------------------------------------------------------------------------------

# list comprehension

# l1 = [i *i for i in range(1,11) if i%2 != 0]
# print(l1)


# set comprehension

# s1 = {i*i for i in range (1,11) if i%2 == 0 }
# print(s1)

# dict comprehension 

# nums = [1,2,3,4,5,6,7]
# d1 = {n:n*n  for n in nums if n % 2 == 0}

# print(d1)

# -----------------------------------------------------------

# Use a dictionary comprehension to build {n: n*n*n} (cubes) for numbers 1 to 6.
# Then look up and print the cube of 4.

nums = [1,2,3,4,5,6]

d1 = {i: i*i*i for i in nums }

print(d1[4])