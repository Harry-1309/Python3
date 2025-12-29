def greatest(my_dict):
    max_bid = 0
    name = ''
    for key in my_dict:
        value = my_dict[key]
        if value>max_bid:
            max_bid = value
            name = key
    return name,max_bid

my_dict={}
while True:
    key = input("What is your name: ")
    value = int(input("What's your bid?:$"))
    my_dict[key] = value
    command = input("Are there any other bidders?: ").lower()
    if command == "no":
        name, bid = greatest(my_dict)
        break
    print("\n"*50)
print(f"The winner is {name} with a bid of ${bid}")
