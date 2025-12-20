def swap_case(s):
    my_string = ""
    for i in s:
        if i.isupper() == True:
            my_string+=i.lower()
        else:
            my_string+=i.upper()
    return my_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



