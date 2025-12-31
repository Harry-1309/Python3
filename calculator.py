def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multipy(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

continue_calc = 'n'
while True:
    if continue_calc == 'n':
        n1 = int(input("What's the first number? "))
        
    if continue_calc == 'n' or 'y':
        print(f"+\n-\n*\n/\n")
        operation = input("Pick an operation: ")
        n2 = int(input("Whats the next number? "))
        if operation == "+":
            final_value = add(n1,n2)
        elif operation == "-":
            final_value = subtract(n1, n2)
        elif operation == "*":
            final_value = multipy(n1,n2)
        elif operation == "/":
            final_value = divide(n1,n2)
        else:
            print("Wrong command")
            continue
        print(f"{n1}{operation}{n2} = {final_value}")
        continue_calc = input(f"Type 'y' to continue calculating with {final_value}, or type 'n' to start a new calculation: ").lower()
        n1 = final_value






