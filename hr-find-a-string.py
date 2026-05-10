def count_substring(string, sub_string):
    count = 0
    length_of_string = len(string)
    length_of_sub_string = len(sub_string)

    for i in range(length_of_string):
        if sub_string == string[i: length_of_sub_string+i]:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
