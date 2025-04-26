




def outer_function(n):
    def inner_func(x,y):
        x=x*2
        y=y+10
        n(x,y)

    return inner_func

@outer_function
def main_function(p,q):
    print(p+q)


s = int(input("enter any no"))
t = int(input("enter any no"))


main_function(s,t)    
    