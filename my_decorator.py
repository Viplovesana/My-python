
"decorator"
# def outer_func(main_func):
#     def inner_func(p,q):
#         p=p*10
#         q=q+40
#         main_func(p,q)
#     return inner_func

# @outer_func
# def main_func(x,y):
#     print(x+y)
# p = int(input("enter any no :"))
# q = int(input("enter any no :"))
# main_func(p,q)

"the normal function"
# def main_function(x,y):
#     print(x*y)
# s=int(input("Enter any no :-"))
# t=int(input("Enter any no :-"))
# main_function(s,t)  


"modify the changes using decorator"

def outer_func(main_func):
    def inner_func(s,t):
        s=s*2
        t=t+2
        main_func(s,t)
    return inner_func 
      
@outer_func

def main_func(p,q):
    print(p+q)
s=int(input("Enter any number :"))
t=int(input("Enter any number :")) 
main_func(s,t)   





