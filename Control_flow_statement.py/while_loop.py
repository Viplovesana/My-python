# n = int(input("enter any number : "))
# i = 1
# while i<=n:
#     if i<n:
#         print(i ,end=",") # end is responsible for the horizontal output because of comma   
#     else:
#         print(i)
#     i = i + 1        


# n = int(input("enter any number : "))
# i = 1
# multi= 1
# while i<=n:
#     multi=multi*i
#     if i<n:
        
#         print(i ,end="*") # end is responsible for the horizontal output because of comma   
#     else:
#         print(i ,end="=")
#     i = i + 1 
# print(multi)   
# 
#     



# n = int(input("enter any number : "))  

# i = 1
# fact = 1

# while i<=n:
#     fact=fact*i
#     i=i+1
#     print("factorial of {} is equal to {}".format(n,fact))





# n = int(input("enter any number : "))  


# x=n
# rev=0
# while n>0:
#     last_digit=n % 10 
#     rev = rev*10+last_digit
#     n=n//10
# print(rev)
# print(n)

# if x==rev:
#     print("paliondrom")
# else:
#     print("not palindrom") 


'print hello...................'

# i = 1
# while i <= 5:
#     print('hello world')
#     i  = i + 1



'wap to print a no from 1 to 5...'

# i = 5
# while i >= 1:
#     print(i)
#     i = i - 1


# print ('loop ended')



'WAP to print a no from 1 to 100'


# i =  1

# while i <= 100:
#     print(i)
#     i = i + 1


# i =  100
# while i>=1:
#     print(i)
#     i = i - 1
# print('loop ended')   
# 
     


'WAP to print multiplication of n no....'

# n = int(input('enter any no :'))

# i =  1n
# while i <= 10:
#     print(n*i)
#     i = i + 1




'WAP to print pelindrom of a string '

'wap to print ar'

# n = int(input("enter any no : "))

# digit_count = 0
# while n>0:
#     n = n // 10
#     digit_count = digit_count +1
# print(digit_count)    



'print thre elements of the following list using a loop'

# num = [5,10,15,20,25,30,35,40,45,50]

# index = 0

# while index<len(num):
#     print(num[index])
#     index=index+1

# heros=['ironman','superman','thor','shaktiman']

# idx =0
# while idx<len(heros):
#     print(idx)
#     idx=idx+1


# '''num = (5,10,15,20,25,30,35,40,45,50)
# x = 50
# i = 0

# while i<len(num):
#     if(num[i]==x):
#         print("found at idx",i)
#     else:
#         print('not found')
    
    
#     i = i +1'''


'using break  and continue method in  while loop....................................'

# i = 0  #break point 
# while i<=10:
#     print(i)
#     if(i == 7):
#         break
#     i = i + 1
# print("loop ended")   



# i = 0   #continue point // it will skip the value wher the condition given...
# while i<=10:
#     if(i==4):
#         i=i+1
#         continue
#     print(i)
#     i=i+1
# print("loop ended " )    



##################   TASK QUESTIONS   ###################
    ##################   TASK QUESTIONS   ###################

                     ######### Print the n Even Number #############

# num=int(input("Enter the number : "))
# i=1
# while (i<=num):
#   if i<num:
#     print(2*i,end=',')
#   else :
#     print(2*i)  
#   i=i+1

                     ########### Print Sum of N Even Number #########

# num=int(input("Enter the number : "))
# i=1
# sum=0
# while (i<=num):
#     sum=sum+(2*i) 
#     if i<num:
#       print(2*i,end=' + ')
#     else :
#       print(2*i,end=" = ")  
#     i=i+1
# print(sum)

     ######### Print the even number from 1 to n ##############

# n=int(input("Enter the Number : "))
# i=1
# while(i<=n):
#     if i<n:
#         if i%2==0:
#           print(i,end=",")
#     else:
#       print(i)
#     i=i+1 

     ######### Print the SUM of even number from 1 to n ##############
     
# n=int(input("Enter the Number : "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+i
#     if i<n:
#         if i%2==0:
#           print(i,end=" + ")
#     else:
#       print(i,end=" = ")
#     i=i+1  
# print(sum)

       #||||||||||||||||||||||||| ODD NUMBER QUESTION ||||||||||||||||||||||||||||||#

                          ######### Print the n Odd Number #############

# num=int(input("Enter the number : "))
# i=1
# while (i<=num):
#   if i<num:
#     print((2*i)-1,end=',')
#   else :
#     print((2*i)-1,end=" ")  
#   i=i+1

                     ########### Print Sum of N Odd Number #########

# num=int(input("Enter the number : "))
# i=1
# sum=0
# while (i<=num):
#     sum=sum+((2*i)-1) 
#     if i<num:
#       print((2*i)-1,end=' + ')
#     else :
#       print((2*i)-1,end=" = ")  
#     i=i+1
# print(sum)

     ######### Print the Odd number from 1 to n ##############

# n=int(input("Enter the Number : "))
# i=1
# while(i<=n):
#     if i<n:
#         if i%2==0:
#           print(i-1,end=",")
#     else:
#       print(i-1,end=" ")
#     i=i+1  

     ######### Print the SUM of Odd number from 1 to n ##############
     
# n=int(input("Enter the Number : "))
# i=1
# sum=0
# while(i<=n):
#     if i<n:
#         if i%2==0:
#           print(i-1,end=" + ")
#         else:
#           sum=sum+i
#     else:
#       print(i-1,end=" = ")
#     i=i+1  
# print(sum)


# num = int(input("enter any no"))

# i = 0
# while i <=num:
#         if( i%2==0):
#              print(i)
   
#         i=i+1
# print("loop ended")        

        
# ........................................................................

# # palimdrom

# n = int(input('Enter any no : '))

# rev = 0 
# x = n

# while n>0:
#     last_digit=n%10

#     rev= rev*10+last_digit

#     n =n//10

#     print(rev)

#     if x == rev:
#         print("palindrom")
#     else:
#         print("not a palindrom")    




#....................................digit of thre no .........................





# n =  int(input("enter any no : "))


# digit_count=0
# while n>0:
#     digit_count=digit_count+1

#     n=n//10
              
    
#............................phibonacchhi series........................    
  
# n=10
# a=0
# b=1
# print(a,b,end=' ')  #......................1st 
# i=3
# while i<=n:
#     z=a+b
#     print(z,end=' ')
#     a,b=b,z
#     i=i+1
 

# n=10
# a=0
# b=1
# print(a,b,end=' ')   #......................2nd method.....
# i=1
# while i<=(n-2):
#     z=a+b
#     print(z,end=" ")
#     a,b=b,z
#     i=i+1


# n=10
# a=0
# b=1
# z=0
# while z<=n:
#     z= a+b
#     print(z,end=" ")
#     a,b=b,z



"WAP to find fibonacci series..."


n = int(input("enter the number :"))
a = 0
b = 1
c = 0
while c<=n:
    print(c)
    a=b
    b=c
    c=a+b 
    










