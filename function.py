

# def add(x,y):
#     return (x+y)

# p = int(input("enter any number :"))
# q = int(input("enter any number :")) 


# z = add(p,q)
# print(z)
# print("hello")
# print(z)



# def even(n):
#     for i in range(2,n,2):
#         print(i)
# x =int(input("enter a number :"))


# even(x)


# def even_or_not(n):
#     if n%2==0:
#         print)
#     else:
#         print(f'given no {n}is odd')
# n=int(input("enter any number :"))
# even_or_not(n)  




def leap_year(n):
    if n%4==0 or n%400==0 and n%100!=0:
     print(f'given no{n}is a leap year')
    else:
          print(f'given no{n}is not leap year' )
n =int(input("enter the year :")) 
leap_year(n)         

         