if __name__ == "__main__":
    n = int(input())
    numbers = tuple(map(int, (input().split())))
    print(hash(numbers))


# The above code is correct but python generates randomise hash values in python 3 in every run/session. Thats why the above code will not get accepted in hackerrank. we need to use the below code
# if __name__ == "__main__":
#     n = int(raw_input()) # Python 2 uses raw_input() for strings
#     # We use map(int, ...) and then convert to a tuple
#     numbers = tuple(map(int, raw_input().split()))
#     print(hash(numbers))
