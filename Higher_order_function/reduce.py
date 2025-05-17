

# import functools

# l = [10,20,30,50,15,25] 

# def max_fan(x,y):
#     if x<y:
#         return x
#     else:
#         return y
# x = functools.reduce(max_fan,l)
# print(x) 

# import functools

# l=[10,20,30,40,50,60]

# def max_no(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# x=functools.reduce(max_no,l) 
# print(x)

"print smallest element from the element"
import functools

l = [45,86,24,87,343,897,45,34,6]

def small_func(x,y):
    if x>y:
        return x
    else:
        return y

x=functools.reduce(small_func,l) 
print(x)  


  





