a=True
b=False
c=True

#logical op - and or 
 
l=a and b 
new_l=a and c 
d=a or b
d1=a or c
d2=a and b and c
d3=a or b or c
print(f"{l,type(l)}\n{new_l,type(new_l)}\n{d,type(d)}\n{d1,type(d1)}\n{d2,type(d2)}\n{d3,type(d3)}")

#not change the value if its true then it will be false

d4 =a and not b
print(d4,type(d4))

age=18
cs=40
cgi=8
print(age>=18 and cgi>7 and cs>40)

#none is considered as a false
print(bool(""))