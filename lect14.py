# the most common way to create a dict is - literals
# student = {"name" : "amit", "age":18, "cgpa":8.75 }
# print(student)

# # empty dict
# empty = {}
# print(empty)
# # using dict constructor
# person = dict(name="neha", city = "varanasi")
# print(person)

# # from pairs
# pairs = dict([("a",1),("b",2)])
# print(pairs)

# student = {"name":"dhanush", "age":18 , "cgpa ": 8.5, "course" : "BCA"}

# for keys in student.keys():
#     print(keys)

# for values in student.values():
#     print(values)

# for items in student.items():
#     print(items)

# ---------------------------------------------------------------------------

# # use add , update and safely read missing key and delete 

# student = {"name" : "dhanush", "age":18,}
# student["course"] = "bca"
# student["age"] = 20
# print(student.get("email"))
# del student["course"]
# print(student)

# --------------------------------------------------------------------------

# given price = {"pen" : 10 , "book": 50 , "bag":60} , loop over it and print each line as "pen cost 10"

# price = {"pen":10, "book":50, "bag":30}
# for k,v in price.items() :
#     print(f"{k} cost {v}")

# -----------------------------------------------------------------------------
# hw 1

# Build a phone book dict with 3 name → number entries. Ask the user for a name
# and print the number using 
# .get() so a missing name prints 
# instead of crashing


# book ={
#     "rajesh" : 9898987476,
#     "rahul" : 7990336750,
#     "ramesh" : 567657890,

# }
# a=str(input("enter name to get the number :"))

# print(a,book.get(a,"not found"))

# -------------------------------------------------------------------------

# hw 3
# Total & Highest
# Given 
# "Not found"
# marks = {"math": 90, "sci": 85, "eng": 78} , use looping to print the
# total marks and the subject with the highest marks.
# marks = {"maths":90 , "sci" : 85 , "eng" : 78}

# total = 0
# highest = 0 
# top_subject = ""
# for k,v in marks.items():
#     total += v 

#     if v > highest:
#         highest = v 
#         top_subject = k

# print ("the total marks are",total)
# print (f"the highest marks are in {top_subject} got {highest}")

 # --------------------------------------------------------------------------

# create a nested dict of 3 student, each with name and gpa .
#  loop over it and print eachstudent's name and gpa . 
# then print the name of the student with the highest gpa

student= {
    "s1" : {"name" : "ganesh" , "GPA" : 10 },
    "s2" : { "name" : "ram" , "GPA" : 9},
    "s3" : {"name": "laksman" , "GPA" : 8}

    }

highest = 0
top_sub = ""
for i , info in student.items():
    print(i,"->",info["name"],"=",info["GPA"])

for k,v  in student.items():

    if v["GPA"] > highest :
        highest = v["GPA"]
        top_sub = v["name"]

print(f"the student with highest score is {top_sub} = {highest} ")

# ------------------------------------------------------------------------------

from collections import Counter

counts = Counter("banana")
print(counts)

print(Counter(counts).most_common(2))