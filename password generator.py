import random

#Easy version

letters = ["a", "b", "c", "d", "e"]
numbers = ['0', '1', '2', '3', '4', '5']
symbols = ['!', '@','#', '$', '%']

passcode = ""

n_letters = int(input())
n_numbers = int(input())
n_symbols = int(input())

for i in range(n_letters):
    let = random.randint(0,len(letters)-1)
    p1 = letters[let]
    passcode += p1

for i in range(n_numbers):
    num = random.randint(0,len(numbers)-1)
    p2 = numbers[num]
    passcode += p2

for i in range(n_symbols):
    sym = random.randint(0,len(symbols)-1)
    p3 = symbols[sym]
    passcode += p3

print(passcode)


#Hard version

my_list = []
my_sum = n_letters + n_numbers + n_symbols
passcode = " "
for i in range(n_letters):
    let = random.randint(0,len(letters)-1)
    p1 = letters[let]
    index = random.randint(0, my_sum-1)
    my_list.insert(index, p1)

for i in range(n_numbers):
    num = random.randint(0,len(numbers)-1)
    p2 = numbers[num]
    index = random.randint(0, my_sum-1)
    my_list.insert(index, p2)

for i in range(n_symbols):
    sym = random.randint(0,len(symbols)-1)
    p3 = symbols[sym]
    index = random.randint(0, my_sum-1)
    my_list.insert(index, p3)

passcode = "".join(my_list)
print(passcode)


# using choice() function

n_letters = int(input())
n_numbers = int(input())
n_symbols = int(input())

my_list = []
my_sum = n_letters + n_numbers + n_symbols
passcode = " "

for i in range(n_letters):
    p1 = random.choice(letters)
    index = random.randint(0, my_sum-1)
    my_list.insert(index, p1)

for i in range(n_numbers):
    p2 = random.choice(numbers)
    index = random.randint(0, my_sum-1)
    my_list.insert(index, p2)

for i in range(n_symbols):
    p3 = random.choice(symbols)
    index = random.randint(0, my_sum-1)
    my_list.insert(index, p3)

passcode = "".join(my_list)
print(passcode)



