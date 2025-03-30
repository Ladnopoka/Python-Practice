def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[-1]
    left = []
    right = []
    middle = []

    for i in array:
        if pivot == i:
            middle.append(i)
        elif pivot > i:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + middle + quick_sort(right)

def main():
    # Step 1: pivot = 9
    # Step 2: left = [5,2,8,1], middle = [9], right = []
    # Step 3: Recursively sort [5,2,8,1]
    # Continue until sorted

    my_array = [5, 2, 8, 1, 9, 10, 0, 11, 3, 19, 100, 6]

    result = quick_sort(my_array)
    print(f"Sorted array: {result}")

if __name__ == "__main__":
    main()