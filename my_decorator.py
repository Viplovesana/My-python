
"constructor"
def outer_func(main_func):
    def inner_func(p,q):
        p=p*10
        q=q+40
        main_func(p,q)
    return inner_func

@outer_func
def main_func(x,y):
    print(x+y)
p = int(input("enter any no :"))
q = int(input("enter any no :"))
main_func(p,q)





