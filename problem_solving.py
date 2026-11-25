# # print 1 to 50 number but if it is divide by 3 is 0 then print fizz and if it is divide by 5 is 0 then buzz if both then print fizzbuzz

# for i in range(1,51):
#     if i%3 == 0 and i%5 == 0:
#         print("fizzbuzz")
#     elif i%3 == 0:
#         print("fizz")
#     elif i%5 == 0 :
#         print("buzz")
#     else :
#         print(i)


# find the average and total do not use sum()

# marks=[85,90,78,67,89,91]
# sum = 0
# for i in marks:
#     sum=sum+i
# avg=sum/len(marks)
# print("sum =",sum)
# print("average =",avg)
 
# #find the largest number without using max funtion

# nums=[45,56,76,89,54,]
# largest = nums[0] 
# for i in nums:
#     if i > largest:
#         largest = i
# print(largest)

#count duplicate
items = [1,2,2,3,4,4,5,6,7,9,7]

dup=[]

for i in items:
    count = 0 

    for j in items:
         if i == j :
            count=count+1
    if count>1 and i not in dup:
            dup.append(i)      


print(dup)

#program to check the prime number 

# n=int(input("enter a number : "))
 
# for i in range(n):
#   if n < 2 :
#     print("do not enter a number 0 or 1")
#     is_prime=True

# for i in range(2,n):
#   if n % i == 0 :
#     is_prime=False

# if is_prime:
#   print("the number is a prime number")
# else:
#  print("enter a valid prime number ")

# n=int(input("enter a number"))
# is_found = False 

# numbers = [12,34,56,76,56,47,78]
# for numbers in range(n):
#     if n == numbers:
#         is_found = True
#         break

 
# if is_found :
#     print("got the number")
# else :
#     print("error 404")
    

    
    
