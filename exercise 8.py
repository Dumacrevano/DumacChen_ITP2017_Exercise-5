import math
a=lambda x:x**2
b=lambda y,z:math.sqrt(y**2+z**2)
c=lambda *args:sum(args)/len(args)
d=lambda string:"".join(set(string))

def A(x):
    return x**2
def B(y,z):
    return math.sqrt(y**2+z**2)
def C (*args):
    return sum(args)/len(args)
def D (string):
    return "".join(set(string))
print(C(1,2,3,4,5,6))