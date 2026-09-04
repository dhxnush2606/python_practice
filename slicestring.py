
s="hello world"
#slicing s[start:stop:step]

print(s[0:5:1])

print(s[0:5:2])

print(s[2:5:1])

#the default value of start and stop is 0 and 1

print(s[:5])
print(s[5:])
print(s[::-1])
#its always count in forward way
print(s[-1::-1])


print(s[:])
print(s[:len(s)])

#strings are immuatable || but can change indirectly
a="Python"
new_a="j"+a[1:]
print(a)
print(new_a)

#concatenation(+)

fname='Dhanush'
mname='Vanniyar'
lname='Armugam'

full=(fname+" "+mname+" "+lname)
print(full)

#repetation(*)
line=('-'*50)
print(line)
#membership test (in/not in)
k='messi is the goat'
g=('goat' in k)
print(k)
print(g)


