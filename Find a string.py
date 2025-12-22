def count_substring(string, sub_string):
    len_substring = len(sub_string)
    count = 0
    for i in range(len(string)):
        if sub_string == string[i: i+len_substring]:
            count+=1
    return count



string = input().strip().upper()
sub_string = input().strip().upper()

count = count_substring(string, sub_string)
print(count)