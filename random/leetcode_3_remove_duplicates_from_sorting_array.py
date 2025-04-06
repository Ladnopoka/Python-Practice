def main():
    str = ["dog","racecar","car"]
    str2 = ["flower","flow","flight"]
    str3 = ["aton","agon","abon"]
    str4 = ["a"]
    str5 = ["abab","aba",""]
    str6 = [0,0,1,1,1,2,2,3,3,4]
    str7 = [1,2]
    result = l1(str6)

    print(result)    

def l1(nums) -> str:
    #Pro Solution
    j = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    return j


    #MY SOLUTION
    # if len(nums) <= 1:
    #     return 1

    # stack = []
    # unique_elements = 0
    # index = 0

    # #for i in range(len(nums)):
    # while index < len(nums):
    #     if nums[index] == '_':
    #         break
    #     elif nums[index] not in stack:
    #         stack.append(nums[index])
    #         unique_elements += 1
    #     elif nums[index] in stack:
    #         nums.pop(index)
    #         nums.append('_')
    #         index -= 1

    #     index += 1

    # print(nums)

    # return unique_elements

if __name__ == "__main__":
    main()  # Run the main function 
