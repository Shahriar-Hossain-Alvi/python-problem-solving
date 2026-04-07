if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    def average(marks):
        average_mark = sum(marks) / len(marks)
        print(f"{average_mark:.2f}")

    average(student_marks[query_name])
