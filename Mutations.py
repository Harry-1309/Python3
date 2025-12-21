def mutate_string(string, position, character):
    #new_string = s[:position] + c + s[position+1:]

    my_list = []
    
    for ind in range(len(s)):
        my_list.append(s[ind])
    my_list[position]=c
    new_string = "".join(my_list)
    
    return new_string

if __name__ == '__main__':
    s = input() #"abracadabra"
    i, c = input().split() #[5, k]
    s_new = mutate_string(s, int(i), c)
    print(s_new)