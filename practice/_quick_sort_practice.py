def quick_sort(array):
    print("aa")
    
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