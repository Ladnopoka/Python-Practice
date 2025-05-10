def removeElement(self, nums: list[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

    
def main():
    nums = [3,2,2,3]
    nums1 = [0,1,2,2,3,0,4,2]
    val = 3
    val1 = 2

    print(removeElement(nums1, val1))

def removeElement(nums: list[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

if __name__ == "__main__":
    main() 