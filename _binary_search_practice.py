def binary_search(array, target):
    left = 0
    right = len(array)-1

    while left <= right:
        mid = left + (right - left)

        if target == array[mid]:
            return mid
        elif target >= array[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def main():
    my_array = [1, 2, 5, 6, 8, 10, 14, 16, 17, 18, 19, 20]
    target = 6

    result = binary_search(my_array, target)
    print("index: ", result)

if __name__ == "__main__":
    main()