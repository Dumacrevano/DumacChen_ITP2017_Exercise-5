import math
def calculator(num_1,num_2,opr="+",out="float"):


        if opr=="+":
            c=num_1+num_2

        elif opr=="-":
            c=num_1-num_2

        elif opr=="*":
            c=num_1*num_2

        elif opr=="/":
            c=num_1/num_2
        else:
            raise ValueError("please input only +,*,/,-")

        if out=="float":
            c=float(c)
        elif out=="int":
            c=math.round(c)
        else:
            raise ValueError("please input int or float")
        return c
print(calculator(int(input("num1")),int(input("num2")),input("insert +,-,/,*"),input("float or interger")))
