if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    #print(student_marks)
    

    query_name = input()
    score = (student_marks[query_name])
    #print(score)
    #print(len(score))
    sum = 0
    avg = 0
    for item in score:
        sum += item
        avg = sum/len(score)
    print(f"{avg:.2f}")