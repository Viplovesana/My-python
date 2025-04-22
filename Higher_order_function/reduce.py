
import functools

# l = [10,20,30,50,15,25] 

# def max_fan(x,y):
#     if x<y:
#         return x
#     else:
#         return y
# x = functools.reduce(max_fan,l)
# print(x)    



l =[1,2,3,4,5,6]

def sum_all(x,y):
    return x+y
x = functools.reduce(sum_all,l)
print(x)

