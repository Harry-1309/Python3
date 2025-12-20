if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner = arr[0]
    runner = arr[0]
    
   

    for item in arr:
        if item > winner:
            winner = item
    #print(winner)
    
    for item in arr:
        if item!= winner and (runner == winner or item > runner):
            runner = item
           
    print(runner) 