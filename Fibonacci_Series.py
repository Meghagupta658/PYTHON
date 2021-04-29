def fib(num):
    if (num < 0):
        print('Number is invalid')
    else:
         a = 0
         b = 1
         print(a)
         print(b)
         for i in range(2,num):
            c = a+b
            a = b
            b = c
            print(c)
           
fib(int(input('enter a number')))          
            

