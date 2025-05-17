
"rectification of the data in a particulat data"



# l =[1,2,3,4,5,6,6,7,8,9,10]

# def evenno(n):
#     if n%2==0:
#         return n
# # x = filter(evenno,l)
# # print(tuple(x))    


# l = [4,7,8,4,6,9,56,3,45,5,3,7]

# def oddno (n):
#     if n%2!=0:
#         return n
# x = filter(oddno,l)
# print(tuple(x))    


# l=[1,2,3,4,5,6,7]
# def even(n):
#     if(n%2==0):
#         return n
# x = filter(even,l)
# print(x)
# print(list(x))


# l=[1,2,3,4,5,6,7]
# def even(n):
#     if(n%2!=0):
#         return n
# x = filter(even,l)
# print(x)
# print(list(x))

"Use filter() to extract even numbers from a list of integers."
# l=[12,3,4,5,6,7,8,9]
# def even_no(n):
#     if n%2==0:
#         return n
# x = filter(even_no,l)
# print(x)
# print(list(x))

"Use filter() to remove all empty strings from a list."
# name=['','viplove','dharmendra','','prem','']
# string=list(filter(None,name))
# print(string)

"Given a list of words, filter out the words with less than 4 characters."
# l=['bob','vip','vikas','sumit','lee']
# def character(n):
#     if len(n)<=4:
#         return n
# x=filter(character,l)
# print(x)
# print(list(x)) 

"rectification of the data in a particulat data"
# l=[3,5,7,2,8]
# def even_no(n):
#     if n%2==0:
#         return n
# x=filter(even_no,l)
# print(x)
# print(list(x))
    

# l=[3,5,7,2,8]
# def odd_no(n):
#     if n%2!=0:
#         return n
# x=filter(odd_no,l)
# print(x)
# print(list(x))


"filter the odd number from the list"
# l=[2,45,7,3,78,96,4,3,66]
# def odd_fun(n):
#     if n%2!=0:
#         return n
# x=filter(odd_fun,l)
# print(tuple(x))    

"Create a lambda function that returns True if a string starts with 'A'. Use it with filter()."
frts=["apple","grapes","banana","avocada","orange"]
def fruits(word):
    return word.startswith("a")
    
x=filter(fruits,frts)
print(list(x))    
    