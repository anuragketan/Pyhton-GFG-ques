#1. Chek if the entered number is Armstrong number
# num=int(input("Enter the number:\n"))
# temp=num
# sum_cube=0
# while(temp>0):
#     sum_cube+=int((temp%10))**3
#     temp/=10
# print(sum_cube)    
# if(num==sum_cube):
#     print("Its a Fibonacci Number.")
# else:
#     print("Sorry, Its not a Fibonacci Number")            

# 2. Find Area of a circle.
# from cmath import pi
# radii=float(input("Enter the radius of the circle:\n"))
# if radii>0:
#     print("Area of the circle is ",pi*(radii**2))
# else:
#     print("Enter a correct radius")    

#3. Print all the Prime numbers in an interval
# intrv1=int(input("Enter starting interval:\n"))
# intrv2=int(input("Enter ending interval:\n"))
# for i in range(intrv1,intrv2+1):
#     count=0
#     for _ in range(1,i+1):
#         if(i%_==0):
#             count+=1 
#     if (count<=2):
#         print(i,"is a prime number")
    
#4. Prog to check whether a number is prime or not
# num=int(input("Enter the number you want to check if its prime or not:\n"))    
# count=0
# for i in range(1,num+1):
#     if(num%i==0):
#         count+=1
# if(count<=2):
#     print(num,"is a prime number")
# else:
#     print(num,"is Composite number")        

#5. Prog to find nth Fibonacci number
# def fibo(n):
#     if n<=0:
#         print("Incorrect Input")
#     elif(n==1):
#         return 0
#     elif(n==2):
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# nth_no=int(input("Enter the nth term for fibonacci:\n"))
# print(fibo(nth_no))