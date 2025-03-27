def binary_search(array, target):
    left = 0
    right = len(array)-1

    while left <= right:
        mid = left + (right - left)//2
        print("Mid: ", mid)
        print("Value: ", array[mid])
        
        if array[mid] == target:
            return array[mid]
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

        print(mid)

    return -1
    

def main():
    print("Testing some stuff")
    print("I am writing this text and jumping to next line")

    #num = 18
    my_array = [1, 2, 5, 6, 8, 10, 14, 16, 17, 18, 19, 20]
    target = 8

    result = binary_search(my_array, target)
    print("End result: ", result)

if __name__ == "__main__":
    main()