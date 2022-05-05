# Basic Questions
# 1. Write a program to add two numbers
try:
    num1 = int(input("Enter first number:\n"))
    num2 = int(input("Enter second number:\n"))
    print("The sum of {} and {} is {}".format(num1,num2,num1+num2))
except ValueError:
    print("Please input valid numbers")

# 2. Write a program to get maximum of numbers        
try:
    x="Y"
    my_list=[]
    while(x=="Y"):
        num=int(input("Enter number :\n"))
        my_list.append(num)
        x=input("Press Y to enter more number otherwise press any key")
    print("The greatest number is",max(my_list))
except ValueError:
    print("Please input valid number")        
        
# 3 . Write a program to print factorial of a number
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
try:    
    num=int(input("Enter the number whose factorial you want: \n"))
    print("Fatorial of {} is {}".format(num,fact(num)))
except ValueError:
    print("Please Enter a Valid Number ")    
 
# 4 . Write a program to print SImple Interest
try:
    princi=float(input("Please eneter the Principal amount: \n"))
    roi=float(input("Please enter the Rate Of Interest: \n"))
    time=float(input("Please enter the duration(in years): \n"))
    print("""
          -----------Simple Interest-----------
          Principal          =  Rs.{}
          Rate of interest   =  {} %
          Time               =  {} years
          Simple Interest    = (P x R x T)/100
                             = ({} x {} x {})/100
                             =  Rs. {}
          """.format(princi,roi,time,princi,roi,time,(princi*roi*time)/100))
except ValueError:
    print("Please input appropriate values")  

# 5 . Write a program to print Compound Interest      
try:
    princi=float(input("Please enter the Principal amount: \n"))
    roi=float(input("Please enter the Rate Of Interest: \n"))
    time=float(input("Please enter the duration(in years): \n"))
    print("""
          -----------Compound Interest-----------
          Principal          =  Rs.{}
          Rate of interest   =  {} %
          Time               =  {} years
          Compound Interest  =  P(1+R/100)^T
                             =  {}x(1+{}/100)^{}
                             =  Rs. {}
          """.format(princi,roi,time,princi,roi,time,princi*((1+roi/100)**time)))
except ValueError:
    print("Please input appropriate values")  
