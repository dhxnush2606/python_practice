#homework check whether the is psoitive,negative or zero
num=int(input("enter a number:"))

if num>0 :
    print("the number is psoitive")
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")
    
elif num<0 :
    print("the number is negative")
    if num%2==0:
            print("the number is even")
    else:
            print("the number is odd")
    

else :
    print("the number is zero ")


    