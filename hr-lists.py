if __name__ == '__main__':
    N = int(input())

    arr = []

    # 1. insert i e
    def insert_value(pos, val):
        arr.insert(pos, val)

    # 2. print
    def print_list():
        print(arr)

    # 3. remove e
    def remove_value(val):
        arr.remove(val)

    # 4. append e
    def append_value(val):
        arr.append(val)

    # 5. sort
    def sort_list():
        arr.sort()

    # 6. pop
    def pop_value():
        arr.pop()

    # 7. reverse
    def reverse_list():
        arr.reverse()

    for i in range(N):
        take_input = (input().split())
        command = take_input[0]

        if command == "print":
            print_list()

        elif command == "sort":
            sort_list()

        elif command == "pop":
            pop_value()

        elif command == "reverse":
            reverse_list()

        elif command == "insert" and len(take_input) == 3:
            insert_value(int(take_input[1]), int(take_input[2]))

        elif command == "remove" and len(take_input) == 2:
            remove_value(int(take_input[1]))

        elif command == "append" and len(take_input) == 2:
            append_value(int(take_input[1]))
