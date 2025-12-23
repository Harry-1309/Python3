def textwrap(string, max_width):
    output = ""
    for i in range(0, len(string), max_width):
        output += string[i:max_width+i]+"\n"
    return output
        

string, max_width = input(), int(input())
result = textwrap(string, max_width)
print(result)

