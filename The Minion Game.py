def minion_game(s):
    Stuart=0
    Kevin=0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        if s[i].lower() in vowels:
            Kevin += score(i,s)
        else:
            Stuart += score(i,s)
    if Stuart>Kevin:
        print(f"Stuart {Stuart}")
    elif Kevin>Stuart:
        print(f'Kevin {Kevin}')
    else:
        print("Draw")

def score(i,s):
    count = 0
    for j in range(i,len(s)):
        count+=1
    return count

s = input()
minion_game(s)