""" project 3: 
add , subtract , multiply , divide two numbers 
concept : functions , def , return , conditions """

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def devide(a,b):
    if b==0:
        return"can't devide by zero"
    return a/b 

print("=== simple calculater ===")
print("1. add ")
print("2. subtract ")
print("3. multiply" )
print("4. divide\n")

choice =input("choice (1-4) : ")
num1 =float(input(" enter first number : = "))
num2 =float(input(" enter secound number : ="))

if choice  == "1 ":
    print(f" resu;t :{ add (num1,num2)}")
elif choice == "2 "    :
    print(f" result : { subtract( num1, num2)}")
elif choice =="3":
    print(f" result : {multiply(num1 , num2 )}")   
elif choice =="4":
    print(f" result : {devide(num1,num2)}")     

else :
    print("invalid choice ")