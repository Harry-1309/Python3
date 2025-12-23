def print_formated(number):
    len_space = len(str(bin(number))) - 2
    
    
    for i in range(1, number+1):
        decimal = str(i).rjust(len_space)
        octal = oct(i)[2:].rjust(len_space)
        hexadecimal = hex(i)[2:].upper().rjust(len_space)
        binary = bin(i)[2:].rjust(len_space)

        print(decimal,octal,hexadecimal,binary)
   

n = int(input())
print_formated(n)