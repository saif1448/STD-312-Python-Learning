t1 = [1,2,3]
t2 = t1

print(t1)
print(t2)
print(id(t1))
print(id(t2))

t2[0] = 100

print(t1)
print(t2)

# alias ----> no value copy is being created ----> the same memory refenced is passed her
# basically t2 and t1 is same here


v1 = [1,2,3]
v2 = v1.copy()  # rather than passing the same memory reference, it is creating the v2 with value of v1 in complete new
print(v1)
print(v2)
print(f'v1 - > {id(v1)}')
print(f'v2 - > {id(v2)}')


v2[0] = 100
print(v1)
print(v2)  # this is called copying --> clone ---> these two will not have same memory reference



if t1 == t2:
    print("Both are same")
else:
    print("Both are different")

if v1 == v2:
    print("v1 is v2")
else:
    print("v1 is not v2")



a = 30
b = a
b = 40

print(a)
print(b)

print(f'a = {id(a)}')
print(f'b = {id(b)}')

if a is b:
    print("a is b")
else:
    print("a is not b")



p = "abc"
q = "abc"
q = "def"
#
print(p)
print(q)

print(f'p --> {id(p)}')
print(f'q --> {id(q)}')

if p is q:
    print("Yes, p is q")
else:
    print("No, p is not q")


x = [1,2,3]
y = x

print(x)
print(y)
print(f'x --> {id(x)}')
print(f'y --> {id(y)}')

y.append(4)
print(x)
print(y)
print(f'x --> {id(x)}')
print(f'y --> {id(y)}')

y = y + [5]
print(x)
print(y)
print(f'x --> {id(x)}')
print(f'y --> {id(y)}')


z = x[:]
x = [1,2,3]
y = x

print(x)
print(y)
print(f'x --> {id(x)}')
print(f'y --> {id(y)}')

y.append(4)
print(x)
print(y)
print(f'x --> {id(x)}')
print(f'y --> {id(y)}')

z = x[:]
print(x)
print(z)
print(f'x --> {id(x)}')
print(f'z --> {id(z)}')
