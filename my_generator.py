
def even(n):
    for i in range (1,n+1):
        yield (2*i)
x = int(input("enter any number :"))

y = even(x)
print(next(y))

print("hello")
print("hi")
print(next(y))
     








# def even(n):
#     for i in range (1,n+1):
#         yield i
# x = int(input("enter any number :"))

# y = even(x)
# print(next(y))     
# print("hello")
# print(next (y))
# print(next(y))


# def table(n):
#     for i in range(2,n+1):
#         yield i

# x= int(input("enter any number:"))

# y = table(x)
# # print(len(list(x)))
# z= next(y)

# # for i in  range(1,11):
# #     print(f' {z} * {i} = {z*i}')  

# z= next(y)

# for i in  range(1,11):
#     print(f' {z} * {i} = {z*i}')  




   