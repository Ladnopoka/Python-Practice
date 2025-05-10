def triplets(nums):
    max_i = -1
    min_j = 9999999
    max_k = 0


    for i in range(len(nums)):
        if max_i < nums[i]:
            max_i = nums[i]
            continue

        if min_j > nums[i]:
            min_j = nums[i]
            continue

        if max_k < nums[i]:
            max_k = nums[i]

    print(f"i: {max_i} | j: {min_j} | k: {max_k}")


def main():
    nums = [12,6,1,2,7]
    nums2 = [1,10,3,4,19]
    nums3 = [1,2,3]

    triplets(nums2)

if __name__ == "__main__":
    main()