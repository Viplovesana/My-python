

# class Calculator:
#     x=10 
   
#     def add(x,y):
#         return x+y
# obj= Calculator
# z= obj.add(10,20)
# print(z)   

# print(obj.x)


class Home:
    def __init__(self,name,contact,address):
        print("constructor called")
        self.n=name
        self.c =contact
        self.a = address
        print(id(self))

obj1 = Home('Name',123,'Bhopal') 
obj1.__init__('viplove',345,'Bhopal')
print(id(obj1))
print(obj1.n)  
print(obj1.c)  
print(obj1.a)     
    

