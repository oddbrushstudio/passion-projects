#Calculator
class Calculator():
        def __init__(self):
            pass

        def addition(self):
            return(a + b)
        
        def subtraction (self):
            return (a - b)
        
        def multiplication (self):
            return (a * b)
        
        def division (self):
            return(a/b)    

calculator =  Calculator()

#Interface
print ('Calculator Menu:' '\n' '1. Addition' '\n' '2. Subtraction' '\n'  '3. Multiplication' '\n'  '4. Division' '\n'  '5. Exit')
operation = int(input("Pick an operation : "))

#Receives users desire
try:
    while operation != 5:
        if operation == 1:
            a = int(input ("Enter first value : "))
            b = int(input ("Enter second value : "))
            print(f"Your answer is {calculator.addition()}")

            
            progress = int(input("Do you want to continue : " '\n' '1. yes' '\n''2. no' '\n' ' --- ' ))
            if progress == 1:
                pass
            if progress == 2:
                break

        elif operation == 2:
            a = int(input ("Enter first value : "))
            b = int(input ("Enter second value : ")) 
            print(f"Your answer is {calculator.subtraction()}")

            progress = int(input("Do you want to continue : " '\n' '1. yes' '\n''2. no' '\n' ' --- ' ))
            if progress == 1:
                pass
            if progress == 2:
                break

        elif operation == 3:
            a = int(input ("Enter first value : "))
            b = int(input ("Enter second value : "))
            print(f"Your answer is {calculator.multiplication()}")

            progress = int(input("Do you want to continue : " '\n' '1. yes' '\n''2. no' '\n' ' --- ' ))
            if progress == 1:
                pass
            if progress == 2:
                break

        elif operation == 4:
            a = int(input ("Enter first value : "))
            b = int(input ("Enter second value : "))
            print(f"Your answer is {calculator.division()}")

            progress = int(input("Do you want to continue : " '\n' '1. yes' '\n''2. no' '\n' ' --- ' ))
            if progress == 1:
                pass
            if progress == 2:
                break

        elif operation not in range(1,5):
            print("Invalid input")
            continue

except ValueError:
    print("Invalid input")
