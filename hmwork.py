#1. Take radius from user, calculate area of circle (hint: 3.14159 * r ** 2) 

a=float(input("enter the value of radius :"))
b=3.14159 * a**2
print(f" the radius is {a} and its area of circle is : {b}\n{type(b)}")

#2. Take temperature in Celsius,convert to Fahrenheit (F = C * 9/5 + 32) 

c=float(input("enter the temperature in celsius :"))
f=(c*9/5)+32
print(f"the {c}c in fahrenheit is {f}")

#3. Take total seconds from user, convert to hours, minutes,seconds (hint: use // and %)

s=int(input("enter the seconds and it will convert into hurs and minutes :"))
d= s // 86400
remaining_s= s % 86400
h=remaining_s // 3600
remaining_s= remaining_s % 3600

m= remaining_s // 60
se= remaining_s % 60
print(f"{d}-days\n{h}-hours\n{m}-minutes\n{se}-seconds")