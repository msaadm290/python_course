company_name = "Insha"

def company():
    global company_name
    company_name = "abc"
    print("Company name ",company_name)


company_name = "Saad"

print("this", company_name)

company()

def addition(num1 , num2):
    print('Addition Result is: ',num1 + num2)


def subtraction(num1, num2):
    print('Subtraction Result is: ',num1 - num2)


def math(operator, num1, num2 ):
    if(operator == "ADD"):
        addition(num1, num2)
    elif(operator == "SUB"):
        subtraction(num1,num2)
    else:
        print("Something wrong")


addition(10,20)

subtraction(60,50)

math("ADDd",30,1000)

def multiplication(num1, num2):
    print ('multiplication result is: ',num1 * num2)

def division(num1, num2 ):
    print ('division result is : ',num1 / num2)

def math(operator, num1, num2 ):
    if(operator == "MUL"):
        multiplication(num1, num2)
    elif(operator == "DIVID"):
        division(num1,num2)
    elif(operator == "ADD"):
        addition(num1,num2)
    elif(operator == "SUB"):
        subtraction(num1,num2)        
    else:
        print("Something wrong")        


multiplication(10,10)    

division(10,10)

math("SUB",10,10)
math("ADD",10,20)
math("MUL",20,20)
math("DIVID",10,30)


company_name = "lafiesta"

def company():
    global company_name
    company_name = "Lafiesta"
    print("company name",company_name)


company_name = "SSFI"

print("this", company_name) 

company()