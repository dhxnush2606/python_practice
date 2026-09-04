#methods

#ex:lower()

s="   hello   wrold     "
s=s.strip()
s=s.capitalize()
print(s)
print(s.find("Hello"))

#replace

a="my name is dhanush, dhanush loves to play football"
print(a.replace("dhanush","kamal",1))
print(a.replace("dhanush","messi "))
print(a.replace("dhanush,","",))

print("-"*30)

#split

b="one two three"
print(b.split())
b1="ten,nine,eight,seven,"
print(b1.split(','))
print(b1.split(',',2))
b2="python is great and java is awesome"
print(b2.split("and",1))
print("-"*50)

#join 
c=['dhanush','is','18','year','old']
print(' '.join(c))
print('-'.join(c))


#fstring
name='dhanush'
score=95.55

print(f"my name is {name} and my makrs is {score}")
print("my name is {} and my marks is {}".format(name,score))

#other ways
name="messi"
sport="football"

c='my name is {} and i love to play {}'
cr=c.format(name,sport)
print(cr)
print('15 into 15 is {}'.format("225"))

#whatever you wrote in the curly brace {} it output is evaluted

print(f"two + two is {2+2}")
print("-"*50)

print("my name is \n dhanush vanniyar")

#after using r the back slace will also appear 

print (r"my name is \n dhanush vanniyar")
print("-"*50)

d="my name is nana and i love banana "
print(d.count("na"))
