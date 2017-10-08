def fac( m ):
   try:
        if m ==1:
            return 1
        if m==2:
            return 2
        else:
            return m * fac( m - 1 )
   except (RecursionError, TypeError):
       return None
print(fac(3))
# An example of a recursive function to
# find the factorial of a number

