while True:

    num1 = str(input("Number 1?:"))
    num2 = str(input("Number 2?:"))
    operation = str(input("operation?"))
    num1op = int(num1)
    num2op = int(num2)

    if operation == "+":
        answer = num1op + num2op
    
    elif operation == "-":
        answer = num1op - num2op
        
    elif operation =="*":
        answer = num1op * num2op
        
    elif operation == "/":
        answer = num1op / num2op
        
    elif operation =="**":
        answer = num1op ** num2op
        

    print(num1, operation, num2,"=", str(answer)) 


