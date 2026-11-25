# ask the user for a number and print its double .
#  wrap it in try/except so that entering text prints "please enter a valid number" instead of crashing .

# try :
#     n = int(input("enter a number :"))
# except ValueError as e :
#     print("buddy there is an value error :",e)

# finally:
#     print("done")

# --------------------------------------------------

#ask for two number and print the result of dividing them .
#  handle both value error (bad input) and zerodivisionerror with clear messages. 

# def intro (a,b):
#     return a // b

# try :
#     a = int(input("enter a number :"))
#     b = int(input("enter another number :"))
#     print(intro(a,b))

# except (ValueError,ZeroDivisionError) as e:
#     print("error",e)

# finally:
#     print("done")

# --------------------------------------------------------------

# safe list access

# items = [10,20,30,40]

# try : 
#     n = int(input("enter an index number :"))
#     print(items[n])

# except (ValueError,IndexError) as e :
#     print("error",e)

# finally:
#     ("done")

# .................................................................

# book = { "dhanush" : "7990339428" , "kamal": 9898746700 , "sathya" : 7984190571  }

# try: 
#     n = str(input("enter a name to find the number : "))
#     print(book[n])

# except KeyError as e :
#     print("error" ,e)

# ...............................................................

# n = input("enter a any form of number and that will be converted into a int ")

# try :
#     a =  int(float(n))
#     print(a)

# except  ValueError as e :
#     print("error :enter a digit " , e )

# finally :
#     print("thanks for using the app")

# .....................................................

# keep asking until they enter a valid number 

# while True:
#     try :
#         n = int(input("enter a number : "))
#         break

#     except  ValueError as e :
#         print ("error : try again , enter a valid number",)

#     finally :
#         print ("thanks for using th app/website")


# .................................................................

# def intro (a):
#    if a < 0 or a > 100 :
#       raise ValueError("bro enter a real age ")
#    return a

# while True :
#     try :
#         n = int(input("enter your age "))
#         intro (n)
#         break
#     except ValueError as e :
#         print("error :",e)

#     finally :
#         print("done")

# ..........................................................

def intro ( a) : 
    if a < 500 :
        raise ValueError("dear customer, you can't withdraw amount less than 500 .")
    elif a >20000 : 
        raise ValueError("dear customer , the account has insufficient balance")
    return a

while True:
    try :
        n = int(input("enter the amount to withdraw :"))
        intro(n)
        break
    except ValueError as e :
        print ( " try again ,error :", e )

    finally :
        print ( "thanks for visiting our SBI bank ")




         
 