'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))

print(mytripler(11))
'''

my_list= [1,2,3,4,5,6]
square_list = [(lambda x: x*x)(y) if y%2 ==0 else (lambda x:x)(y) for y in my_list  ]


print(square_list)