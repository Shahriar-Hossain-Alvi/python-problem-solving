if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))[:n]

    arr.sort(reverse=True)

    biggest_num = arr[0]

    for i in range(len(arr)):
        if arr[i] < biggest_num:
            print(arr[i])
            break
