#   function in python
# function is named logic which can be re-used

# def area(lenght,width):
#     area = lenght*width
#     return area

# print(area(10,15))
# ------------------------------------------------------------------------------------

# def greet(name,msg="welcome brother"):
#     print(" hello, how are you?",name,"!")
#     print(msg)

# greet("dhanush")

# -----------------------------------------------------------------------------------
# def is_even(num):
#     return num%2 == 0

# print(is_even(int(input("enter a number :"))))
# --------------------------------------------------------------------------------

# def intro(p,r,t):
#     intro = p*r*t / 100
#     return intro

# p = int(input("enter the principle amount :"))
# r = int(input("enter the rate amount : "))
# t = int(input("enter the time :"))

# print(intro(p,r,t))

# ------------------------------------------------------------------------

# write a function to find largest of three numbers without using max()

# def intro(n1,n2,n3):
#     if n1 >= n2 and n1 >=n3:
#         print("the largest number is ",n1)
#     elif n2 >= n1 and n2 >= n3 :
#         print("the largest number is ",n2)
#     else :
#         print("the largest number is ",n3)
       


# a=(int(input("enter a number  :")))
# b=(int(input("enter a another number  :")))
# c=(int(input("enter a  anothernumber  :")))

# intro(a,b,c) 

# --------------------------------------------------------------------------

# def intro(num):
#     total = sum(num)
#     return total,total / len(num)

# s,a = intro([5,6,76,3,4,23,45])
# print(f"the sum of average is :{s} and the average is :{a}")

# -----------------------------------------------------------------

# write a function stats(nums) that return Both the sum and the average as a tuple,
#  call it and upack the result into two variables in one line, then print them,


# def stats(nums):

#     total = sum(nums)
#     average = sum(nums) / len(nums)
#     return total,average 

# l1 = [4,3,2,5,54,6,65]

# total_sum,average_sum =stats(l1)

# print(total_sum)
# print(average_sum)

# ----------------------------------------------------------------

# def area(lenght, width):
#     """return the area of given data """
#     return lenght*width


# print(area.__doc__)

# --------------------------------------------------------------------

# write a function divide(a,b) that return both the quotient and the remaider as a tuple.
#  Unpack and print them for divide(17,5) expectedd 3 and 2

# def divide(a,b):
#     return a // b, a%b


# q,r = divide(17,5)

# print(q)
# print(r)

# ------------------------------------------------------------------

# legb-LOCAL,ENCLOSING,GLOBAL,BUILT-IN

# x="global"

# def outer():
#     x = "enclosing"
#     def inner():
#         x = "local"
#         print(x)
#     inner()
# outer()       

# --------------------------------------------------------------------

#write a function that return min max and average  add a doctstring.
# unpack all three and print them .

# def summary(nums):
#     """"finding a min max and average but output is not in tuple"""
#     return min(nums),max(nums),sum(nums)/len(nums)

# l = [4,5,6,7,34,98,76]
# m1,m2,a1 = summary(l)
# print(f"the min is :{m1}, \n the max is :{m2}, \n and the average is :{a1}")
# print(summary.__doc__)

# ------------------------------------------------------------------------

# importing function from another file 
import mymath
from mymath import add,multiply,is_prime

print(add(2,45))
print(multiply(5,6))
print(mymath.is_prime(89))
