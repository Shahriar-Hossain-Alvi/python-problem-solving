if __name__ == '__main__':
    all_data = []
    second_lowest_grades = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        # make a list with the students name and mark
        student_data = [name, score]

        all_data.append(student_data)  # add the list inside all_data list

    # sort in ascending order based on the marks x[1] => targets the second value inside the sublist
    all_data.sort(key=lambda x: x[1])
    smallest_mark = all_data[0][1]  # store the smallest mark for comparison

    for student in all_data:
        student_name = student[0]
        student_score = student[1]

        # if not mark exists in new array, store the current mark (which is bigger than the smallest mark)
        if len(second_lowest_grades) == 0 and student_score > smallest_mark:
            # store both name and mark
            second_lowest_grades.append(student)
            continue

        # compare with the second smallest mark in the array and add if both are equal
        elif student_score > smallest_mark and student_score == second_lowest_grades[0][1]:
            second_lowest_grades.append(student)

    # print the names alphabetically
    second_lowest_grades.sort()
    for student in second_lowest_grades:
        print(student[0])
