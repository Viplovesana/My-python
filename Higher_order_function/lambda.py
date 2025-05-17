


import functools


x = lambda p,q : (p+q)


r = int(input("enter any no"))
s =int(input("enter any no"))

z = x(r,s)
print(z)


l =[2,4,6,8,10]

x = list(map(lambda x: x**2 ,l))
print(x)


l= [1,2,3,4,5,6,7,8,9]
def even_no(x):
   
    if x%2==0:
        return x
x = filter(even_no,l)
print(list(x)) 

x1 = list(filter(lambda x : x%2==0 ,l))
print(x1)


x = functools.reduce(lambda a,b:a if a<b else b ,l)
print(x)