

# class Calculator:
#     x=10 
   
#     def add(x,y):
#         return x+y
# obj= Calculator
# z= obj.add(10,20)
# print(z)   

# print(obj.x)


# class Home:
#     def __init__(self,name,contact,address):
#         print("constructor called")
#         self.n=name
#         self.c =contact
#         self.a = address
#         print(id(self))

# obj1 = Home('Name',123,'Bhopal') 
# obj1.__init__('viplove',345,'Bhopal')
# print(id(obj1))
# print(obj1.n)  
# print(obj1.c)  
# print(obj1.a)     
    


# class Student:
#     name="viplove sana"
#     subject="python"
#     address="cybrom"
# obj1=Student()
# print(obj1) 
# print(obj1.name)   
# print(obj1.subject)
# print(obj1.address)
# obj2=Student()
# print(obj2.name)




# class Car:
#     brand="toyota"
# obj=Car
# print(obj.brand)   



# class Calculator:
#     x = 10
#     def add(x,y):
#         return x+y
#     print(x)
 

# object=Calculator
# a=object.add(20,30)
# print(a)



# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
      
#     def start_engine(self):
#         print(f"{self.brand} engine started.")   

#     def stop_engine(self):
#         print(f"{self.model} engine stop")    

# my_car=Car("Tata","Nexon")
# my_car.start_engine()
# my_car.stop_engine()


class Student:
   
    def __init__(self,fullname,numbers):  
  
        self.name=fullname
        self.marks=numbers
    
       
s1=Student("viplove sana",95)
print(s1.name,s1.marks)
s2=Student("karan",85)
print(s2.name,s2.marks)
