if __name__ == '__main__':
    my_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append([name,score])
    #print(my_list)
    
    least = my_list[0][1]
    for item in my_list:
        if item[1] < least:
            least = item[1]

    second_least = my_list[0][1]
    for item in my_list:
        if item[1] != least and (second_least == least or item[1]< second_least):
            second_least = item[1]
    
    output = []
    for item in my_list:
        if item[1] == second_least:
            output.append(item[0])
   

    output.sort()
    for item in output:
        print(item)

    