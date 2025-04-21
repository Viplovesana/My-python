
import functools

l = [10,20,30,50,15,25]

def max_fan(x,y):
    if x<y:
        return x
    else:
        return y
x = functools.reduce(max_fan,l)
print(x)    