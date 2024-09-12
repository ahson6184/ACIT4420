#Number of elements
n=int(input("Enter the number of elemnets in the list:"))

my_list=[]

for i in range(n):
    x=int(input("Enter an elment in the list:"))
    my_list.append(x)
print("numbers =",my_list)

'''
result =  [my_list[i]**2 if my_list[i] % 2 == 0
     else my_list[i] for i in range(len(my_list))]


def my_func(x):
    if x%2==0:
        return x*x
    else:
        return x 
''' 

#using list comprehensiom and lambda
result1 = [(lambda x: x*x)(y) if y%2 ==0 else (lambda x:x)(y) for y in my_list ]

# using user_defined function in map 
#result1= map(my_func,my_list)

#my_lambda = lambda x : x*x if(x%2==0) else x

#using lambda in map
result2=map(lambda x : x*x if(x%2==0) else x, my_list)

#using listcomprehension only
result3=[x*x if x%2==0 else x*1 for x in my_list] 


print(list(result1))
print(list(result2))
print(result3)
