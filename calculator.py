def add(x,y):
    result= x,y

def subtract(x,y):
    result= x-y

def multiply(x,y):
    result=x*y

def divide(x,y):
    result=x/y

print("Please select one of the following.")
print("a Add")
print("b Subtract")
print("c Multiply")
print("d Divide")

input("Please enter your choice a/b/c/d:")

num_1=int(input("Please enter your first number:"))
num_2=int(input("Please enter your second number:"))

if add=='a':
    function(num_1,"+",num_2, "=", add(num_1,num_2))
elif subtract=='b':
     function(num_1,"-",num_2, "=", subtract(num_1,num_2))
elif multiply=='c':
    function(num_1,"*",num_2, "=", multiply(num_1,num_2))
elif divide=='d':
    function(num_1,"/",num_2, "=", divide(num_1,num_2))
except ValueError:
    print("enter numbers like 1 and 2")
except ZeroDivisionError:\
    print("Don't divide by zero")