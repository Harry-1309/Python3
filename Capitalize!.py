
def solve(s):
    for i in range(len(s)):
        if s[i]!=" " and (s[i-1]==" " or i==0):
            s = s[:i]+s[i].upper()+s[i+1:]
    return s
s = input()
result = solve(s)
print(result)


# using list
def solve(s):
    output =""
    my_list = s.split(" ")
    for item in my_list:
        output+=item.capitalize()+" "
    return output
s = input()
result = solve(s)
print(result)