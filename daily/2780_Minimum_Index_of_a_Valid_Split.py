def minimumIndex(arr):
    my_dict = {}
    
    for i in range(len(arr)):
        if arr[i] not in my_dict:
            my_dict[arr[i]] = 1
        else:
            my_dict[arr[i]] += 1

    dominant_number = max(my_dict, key=my_dict.get)
    frequency = max(my_dict.values())

    f1 = 0
    f2 = dominant_number

    print(f"Dom num: {dominant_number}")
    print(f"Array: {arr}")
    for i in range(len(arr)-1):
        left = arr[0 : i]
        right = arr[i: (len(arr))]

        print(f"{left} | {right}")
        print(f"f1: {f1}   f2: {f2}")

        if arr[i] == dominant_number:
            f1 += 1
        
        f2 = frequency - f1

        
        print(f"Left len: {len(left)}   Right len: : {len(right)}")
        print(f"Left len: {(i+1)//2}   Right len: : {len(arr)-(i+1)//2}")

        if f1 > (i+1)//2 and f2 > (len(arr)-(i+1))//2:
            return i

        # if f1 > len(left)//2 and f2 > len(right)//2:
        #     return i
        
    return -1



def main():
    arr = [1,2,2,2]
    arr2 = [2,1,3,1,1,1,7,1,2,1]
    arr3 = [3,3,3,3,7,2,2]
    
    result = minimumIndex(arr)
    print(result)
 
if __name__ == "__main__":
    main()