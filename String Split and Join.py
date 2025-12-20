def split_and_join(line):
    # write your code here
    my_list = line.split(" ")
    a = "-".join(my_list)
    return a


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)