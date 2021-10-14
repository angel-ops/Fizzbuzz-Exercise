#Exercise "fizzbuzz" for method
#for number in range(1,21):
#    if (number % 3 == 0) and (number % 5 == 0):
#        print("fizzbuzz")
#    elif number % 3 == 0:
#        print("fizz")
#    elif number % 5 == 0:
#        print("buzz")
#    else:
#        print(number)

#Exercise "fizzbuzz" while method:
number=1
while number <= 100:
    if (number % 3 == 0) and (number % 5 == 0):
        print("fizzbuzz") 
        number = number + 1
    elif number % 3 == 0:
        print("fizz")
        number = number + 1
    elif number % 5 == 0:
        print ("buzz")
        number = number + 1
    else:
        print(number) 
        number = number + 1
