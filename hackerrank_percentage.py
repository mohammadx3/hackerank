def score_avg(scores: list) -> float:
    return sum(scores)/len(scores)
    pass

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks)
    ans = score_avg(student_marks[query_name])
    print(sum(student_marks[query_name]))
    print(f'{ans:.2f}')