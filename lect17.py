# nums = [1,2,3,4,5]

# double = list(map(lambda a:a+a,nums))

# print(double)

# ----------------------------------------------------------

# nums = [-3,-4,5,0,8,-1,4]

# print(list(filter(lambda a : a>=0,nums)))

# ------------------------------------------------------------

# cube = lambda n : n ** 3 

# print (cube(3))

# # -------------------------------------------------------------
# words = ["python","lambda","map"]

# print(list(map(lambda a : a.upper(),words)))

# -----------------------------------------------------------

    
# odd = (tuple(filter(lambda a :a%2 != 0 , range (1,21) )))

# print(odd)

# ---------------------------------------------------------
# from functools import reduce
# nums = [5,10,15,20]

# total = reduce(lambda a,b : a+b , nums)

# print(total)

# -----------------------------------------------------------

# names = ["amit", "neha","ravi ", "sara"]

# ll = sorted(names,key=lambda n : n[-1])

# print(ll)

# ---------------------------------------------------------------

raw = ["$250","$300","$80"]


b=list(map(lambda a : int(a.replace("$","")),raw))
print(b)