

# class Calculator:
#     x=10 
   
#     def add(x,y):
#         return x+y
# obj= Calculator
# z= obj.add(10,20)
# print(z)   

# print(Calculator.x)


# class Home:
#     def __init__(self,name,contact,address):
#         print("constructor called")
#         self.n=name
#         self.c =contact
#         self.a = address
#         print(id(self))

# obj1 = Home('Name',123,'Bhopal') 
# # obj1.__init__('viplove',345,'Bhopal')
# print(id(obj1))
# print(obj1.n)  
# print(obj1.c)  
# print(obj1.a)     
    


# class Student:
#     def __init__(self,fullname,age):
#         self.name=fullname
#         self.age=age

# s1 = Student('viplove sana',23)
# print(s1.name)
# print (s1.age) 
# s2=Student('rohan malakar',22)
# print(s2.name)
# print(s2.age)  



# class Student:
# # 
#     collage_name="rgpv"   #class attributes
#     name="anonymous"
#     def __init__(self,fullname,age):
#         self.name=fullname     #objecty attributes    //if the class name and object name is same   
#         self.age=age                                  #then the preference goes to the ob jects only    

# s1 = Student('viplove sana',23)
# # print(s1.name)
# # print (s1.age) 
# # s2=Student('rohan malakar',22)
# # print(s2.name)
# # print(s2.age) 
# print(s1.collage_name)
# print(Student.collage_name)
# print(s1.name)


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


# class Student:
   
#     def __init__(self,fullname,numbers):  
  
#         self.name=fullname
#         self.marks=numbers
    
       
# s1=Student("viplove sana",95)
# print(s1.name,s1.marks)
# s2=Student("karan",85)
# print(s2.name,s2.marks)



# class Student:
#     school='SHSS'
#     def __init__(self,name,email,add):
#         self.name=name
#         self.email=email
#         self.add=add
#     def show_details(self): 
#         principal="python"       #.......local variable
#         print(self.name,self.email,self.add)
# obj=Student('viplove','viploveasana90@gmail.com','bhopal')
# obj.show_details()
# print(obj.school)
# print(obj.add,obj.name,obj.email) 
# print(obj.principal)       
                  

# class Student():
#     school='SHSS'   #static/class variable
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         Student.city ='bhopal' #static/class variable

#     def add_more(self):
#         Student.greed ='10th' # static/class variable

#     def show_detail(self):
#         print(Student.school,Student.city,Student.city1,Student.greed)


    
        
# obj=Student('viplove',23) 
# obj.add_more()
# Student.city1='indore'
# obj.show_detail()

# q= 50
# class Student:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#         z=10   #local variable we can declare the local variable in the constructor
#         print(z)
#     def show(self):
#         p = 10
#         print(p) 
#         print(q)
         


# obj= Student(10,20)
# obj.show()    



# class Student:
#     school="SHSS"
#     gread ="10th"
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age

#     @classmethod
#     def update_school(cls,sch):
#         cls.school=sch 
#     @classmethod
#     def update_gread(cls,grd):
#         cls.gread=grd
#     @staticmethod
#     def new(x,y):
#         print(x+y)
#     def show_details(self):
#         print(self.n)
#         print(self.a)
#         print(Student.school)
#         print(Student.gread)
# obj=Student('viplove',23)
# obj.show_details()
          
# obj.new(5,4) 
# Student.update_school("st.thomas")
# Student.update_gread("12th")
# obj.show_details()                
    



# class Student:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age

#     def show_data(self):
#         print(self.name)
#         print(self.age)
# obj=Student("viplove",23)   
         



# class Student:
#    "this is demo data"
#    x=10
#    y=20
#    def new (self):
#       print("helllo")
#       print(id(self))


# print(Student.__module__)
# print(Student.__doc__)
# print(Student.__dict__)
# print(id(Student))

# obj=Student()
# print(id(obj))
# obj.new()        



# def outer(main):
#     def inner():
#         print("from inner")
#     return inner
# x = outer(10)
# print(id(x))
# print(id(outer))




"......................................INHERITENCE..........................................................."
    
# class P:
#     def __init__(self,bank,house):
#         self.bank=bank
#         self.house=house
# class C(P):
#     def __init__(self, bank1, house1):
#         self.bank1=bank1
#         self.house1=house1

#     def show_property(self):
#         print(self.bank,self.house)
#         print(self.bank1,self.house1)

# obj=P('HDFC','MP')
# obj1=C('IDFC','kolar')
# obj1.show_property()      



    
# class P:
#     def __init__(self,bank,house):
#         self.bank=bank
#         self.house=house
# class C(P):
   

#     def show_property(self):
#         print(self.bank,self.house)
#         print(self.bank1,self.house1)

# obj=C
# obj=C()



    
# class P:
#     def __init__(self,bank,house,x):
#         self.bank=bank
#         self.house=house
#         self.x=x
# class C(P):
   

#     def show(self):
#         print(self.bank,self.house,self.x)
       

# obj=C('HDFC','KOLAR',100)
# obj.show()


# class P:
   
#     def __init__(self,bank,house,x):
#         self.bank=bank
#         self.house=house
#         self.x=x
# class C(P):
#     def add(self):
#         print("from add class") 
   

#     def show(self):
#         print(self.bank,self.house,self.x)
#     def add(self):
#         print("from add class")    
       

# obj=C('HDFC','KOLAR',100)
# obj.show()
# obj.add()



# class P:
#     def add(self):
#         print("from add class")          
   
#     def __init__(self,bank,house,x):
#         self.bank=bank
#         self.house=house
#         self.x=x
# class C(P):
#     def add(self):
#         super().add()
#         print("from child class") 
#     def show(self):
#         print(self.bank,self.house,self.x)
        
       

# obj=C('HDFC','KOLAR',100)
# obj.show()
# obj.add()


"..................Single _level_inheritance................................."

# class A:
#     def first(self):
#         print("from parent class")
# class B(A):
#     def second(self):
#         print("from child class")  
# obj=B()
# obj.first()
# obj.second()   



".....................Multi_level_inheritance.................................."
# class A:
#     def first(self):
#         print("from grandparent class")
# class B(A):
#     def second(self):
#         print("from parent class")
# class C(B):
#     pass          
# obj=B()
# obj.first()
# obj.second() 

".....................Multiple_inheritance.................................."
# class A:
#     def first(self):
#         print("from Father class")
# class B:
#     def second(self):
#         print("from Mother class")
# class C(A,B):
#     def third(self):
#         print("both father and father classes")

# obj=C()
# obj.first()
# obj.second()
# obj.third()               
            

"..........................Hierarchical inheritence.........................."


# class Parent:
#     def home(self):
#         print("from parent class")
#     def bank(self):
#         print("from parent bank")

# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass

# obj1=Child1()
# obj2=Child2()
# obj1.home()
# obj2.home()
# obj1.bank()
# obj2.bank()




"..........................Hybrid inheritence............................."

# class Grandparent:
#     def home(self):
#         print("from grandparent class")
#     def bank(self):
#         print("from grandparent bank")  


# class Parent1(Grandparent):
#     def car(self):
#         print("car from parent1 class")
# class Parent2(Grandparent):
#     def car2(self):
#         print("car2 from parent2 class")

# class Child(Parent1,Parent2):
#     pass


# obj=Child()
# obj.car()
# obj.car2()
# obj.home()
# obj.bank()

# "............................(MRO)method resolution method.........................."

# class Grandparent:
#     def home(self):
#         print("from grandparent class")
#     def bank(self):
#         print("from grandparent bank")  


# class Parent1(Grandparent):
#     def car(self):
#         print("car from parent1 class")
# class Parent2(Grandparent):
#     def car(self):
#         print("car2 from parent2 class")

# class Child(Parent1,Parent2):
#     pass


# obj=Child()
# obj.car()
# obj.home()
# obj.bank()


"******************************ABSTRACTIONS**************************************************"

# from abc import ABC,abstractmethod

# class A(ABC):
#     def first(self):
#         print("from first method")
        
         
#     @abstractmethod
#     def second(self):
#         pass
#     @abstractmethod
#     def third(self):
#         pass


# from abc import ABC,abstractmethod
# class Senior(ABC):
#     def add(self,x,y):
#         return x+y
#     def sub(self,x,y):
#         return x-y
#     @abstractmethod
#     def div(self):
#         pass
# class junior(Senior):
#     def multi(self,x,y):
#         return x*y
#     def div(self,x,y):
#         return x/y
    
# obj=junior()
# v=obj.multi(10,20)
# c=obj.div(30,29)
# print(v)
# print(c)     


"*************************POLYMORPHISM*************************"


# class A:
#     def add(self,x,y):
#         return(x+y)
#     def add(self,x,y,z):
#         return (x+y+z)
#     def add(self,*n):
#         sum=0
#         for i in n:\
#         sum=sum+1
#     print(sum)


# obj=A()
# obj.add()
# obj.add(1)
# obj.add(1,2,3,4,5) 




"normal Class and Object"
class Car:
    color="mehrun"
    brand="toyata"
car1=Car()
print(car1.brand,car1.color)
    
 





