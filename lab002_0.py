num= int(input("Enter a number: ")) 

if  num > 0 and num % 2 == 0 :
  print("The number is positive and even")
elif  0 < num % 2 == 1 :
    print ("The number is positive and odd")
elif num < 0:
    print("The number is negative.")
else :
    print("The number is zero.")
    