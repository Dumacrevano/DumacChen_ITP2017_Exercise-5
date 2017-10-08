def dum_gen(n):
    x=n
    while x>=0:
        yield x
        x-=1
y=dum_gen(5)
print(type(y))
for z in y:
    print(z)
