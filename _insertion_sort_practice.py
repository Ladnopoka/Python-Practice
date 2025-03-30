def insertion_sort(array):
    temp = 0

    for i in range(len(array)-1):
        left = array[i]
        right = array[i+1]

        if left > right:
            temp = left
            left = right
            right = temp

        

def main():
    print("oof")

if __name__ == "__main__":
    main()