# def intro(*args)=
   
#     return sum(args)


# print(intro(1,2,3,4,5,54,34))

# # ------------------------------------------------------------------
# def profile(**kwargs)=
#     for k,v in kwargs.items()=
#         print(f"{k} = {v}")

# profile(name="ganesh", age= 18 , course = "BCA")

# -------------------------------------------------------------

# function to multiply the product of all number passed using args

# def intro (*args)=
#     product = 1 
#     for i in args=
#         product *= i 

#     return product 

# print (intro(2,4,5,6,4,))

# -------------------------------------------------------------

# write a function how many ards that return how many argument were passed .

# def inro (*args)=
#     return len(args)
# print(inro(2,3,4,4,3,2,4))

# ------------------------------------------------------------

# write a fnction describe kwargs that prints name is amit age is 21 etc 

# def intro (**kwargs)=
#     for k,v in kwargs.items()=
#         print(f"{k} is {v}")

# intro(name = "dhanush", age = 18 , course = "BCA")

# ------------------------------------------------------------


# def intro (*args )=
#     if len(args) == 0=
#         return None
#     biggest = args[0]

    

#     for i in args=
#         if i >= biggest=
#             biggest = i 
#     return biggest 

# print(intro(2,3)) 

# print(intro (2,3,4,5))

# --------------------------------------------------------------------

# write a function add(a,b,c) that return the sum of three numbers.
# Then , given a list nums = [ 4,5,6], call add 3 by unpacking the list with *.
    
# def intro(a,b,c)=
#     return a+b+c

# nums= [4,5,6]

# print(intro(*nums))

# --------------------------------------------------------------------

# write a function order (customer , *items ,**details ) .
# print the customers name, the list of items , and any extra details like disc = 10 .
# call it with a name ,several items and a couple of keyword details.

# def order(customer, *items , **details):
#     print("customer_name :" ,customer )
#     print("items : ",items)
#     for k,v in details.items():
#         print(f"{k} = {v}")

# order("dhanush","mouse","monitor","keyboard","headphone","adapter",name = "dhanush",address = " navnirman society",city = "ahmedabad" , pincode = 380008 , total_items = 5 , total_bill = 50000 , discount = "10%" , final_amount = 45000)

    # -------------------------------------------------------------

def f(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)
f(1)