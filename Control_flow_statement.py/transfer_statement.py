

# x = int(input("enter any number :"))
# y = int(input("enter any number :"))
# z = int(input("enter any number :"))
# p = int(input("enter any number :"))
# h = max(x,y,z,p)
# print(h)
# while(True):
#     if h%x==0 and h%y==0 and h%z==0 and h%p==0:
#         lcm = h
#         break  # break is used for the exit code from the body
#     h = h + 1
# print(f'lcm of given value {x},{y},{z},{p} is {h}')    






# x = int(input("enter any number :"))
# i = 0
# while i<=x:     
#     if i==5:
#         i =i +1
#         break
#     print(i)
#     i=i+1


x = int(input("enter any number :"))
y = int(input("enter any number :"))
z = int(input("enter any number :"))
p = int(input("enter any number :"))  

mv =  min(x,y)

for i in range(1,mv):
    if x%i==0 and y%i==0 and z%i==0 and p%i==0:
        hcf= i
print(hcf)        