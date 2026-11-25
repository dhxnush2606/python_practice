
# nums = [5,2,3,6,1,8]
# nums.sort()
# nums.sort(reverse=True)
# nums.sort(reverse=False) #this is the method whenever (.)comes then its called method
# new_list = sorted(nums)    # here function is sed so that the original data doen't change 
# print(new_list)
# print(nums)

#list comprehension 
# square= [i ** 2 for i in range(1,6) if i ** 2 == 0]
# print(square)

# names =["Ravi","amit","sara","deep"]
# caps =[n for n in names if n[0]. isupper()]
# print(caps)

#nested list comprehension

# matrix = [[1,2,3,],[4,5,6]]
# flat=[num for column in matrix for num in column]
# print(flat)

# grid =[[r * c for c in range(1,4)]for r in range (1,4)]
# print(grid)

# square of even number

# even = [ i **2 for i in range(1,21) if i % 2 == 0]
# print(even)

# sort and find position,sort in descending order and then print the position of particular index in sorted list
 
# scores = [52,90,72,88,60]
# scores.sort(reverse=True) 

# print(f"{scores} \n  \n ")

# flated nested list comprehension 
# matrix = [[1,2],[3,4],[5,6]]


# flated = [ n for row in matrix for n in row]
# print(flated)

# matrix = [[1,2],[3,4],[5,6]]
# flat = []

# for row in matrix:
#     flat.extend(row)

# print(flat)

i = 0 

if i ==0:
    print("zero")
else :
   if i%2 == 0 :
    print("even")
   else :
      print("ODD")

#in a single line 

j = 10 
print("zero" if j == 0 else "even" if j % 2 == 0 else "odd")
