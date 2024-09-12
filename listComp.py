numbers = [1,2,3,4,5,6]
doubled = [x *2 for x in numbers]
print(doubled)

lis =  [x*x if x % 2 == 0
        else  x*1 for i in (len(numbers)]
print(lis)

