import math
def calculator( opr="+", out="float",*num):
    if not num:
        raise ValueError("please enter a number")
    res=num[0]
    for x in num[1:]:
        if opr == "+":
            res += x

        elif opr == "-":
            res -= x

        elif opr == "*":
            res*= x

        elif opr == "/":
            res/= x
        else:
            raise ValueError("please input only +,*,/,-")

    if out == "float":
        c = float(res)
    elif out == "int":
        c = int(res)
    else:
        raise ValueError("please input int or float")
    return c

print(calculator((input("operator")), (input("float/int")), int(input("num"))))

