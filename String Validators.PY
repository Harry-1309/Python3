def alphanumeric(s):
    for i in range (len(s)):
        if s[i].isalnum() == True:
            output1 = "True"
            break
        else:
            output1 = "False"
    return output1

def alpha(s):
    for i in range (len(s)):
        if s[i].isalpha() == True:
            output2 = "True"
            break
        else:
            output2 = "False"
    return output2

def digit(s):
    for i in range (len(s)):
        if s[i].isdigit() == True:
            output3 = "True"
            break
        else:
            output3 = "False"
    return output3

def lower(s):
    for i in range (len(s)):
        if s[i].islower() == True:
            output4 = "True"
            break
        else:
            output4 = "False"
    return output4

def upper(s):
    for i in range (len(s)):
        if s[i].isupper() == True:
            output5 = "True"
            break
        else:
            output5= "False"
    return output5

s = input().strip()
output1 = alphanumeric(s)
output2 = alpha(s)
output3 = digit(s)
output4 = lower(s)
output5 = upper(s)

print(f"{output1}\n{output2}\n{output3}\n{output4}\n{output5}")