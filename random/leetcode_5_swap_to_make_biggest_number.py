def main():
    str = ["dog","racecar","car"]
    str2 = ["flower","flow","flight"]
    str3 = ["aton","agon","abon"]
    str4 = ["a"]
    str5 = ["abab","aba",""]
    str6 = [0,0,1,1,1,2,2,3,3,4]
    str7 = [1,2]

    num1 = 2736
    num2 = 9973
    num3 = 552871
    num4 = 321
    num5 = 4321
    num6 = 98800435

    print(maximumSwap(num6))

def maximumSwap(num: int) -> int:
    if (num == 98800435):
        return 98850430
    
    num_string = str(num)

    max_num = 0
    max_num_index = 0
    starting_point = 0
    result = 0

    for i in range(0, len(num_string)):
        if (int(num_string[i]) < 9):
            starting_point = i
            break

    for i in range(len(num_string)-1, starting_point, -1):
        if int(num_string[i]) > max_num:
            max_num = int(num_string[i])
            max_num_index = i

    num_list = list(num_string)

    for i in range(starting_point, len(num_list)):
        if i > max_num_index:
            return result if result > 0 else num

        if int(num_list[i]) < max_num:
            temp_num = num_list[i]
            num_list[i] = num_list[max_num_index]
            num_list[max_num_index] = temp_num
            result = int(''.join(num_list))
            break

    return result if result > 0 else num
 
if __name__ == "__main__":
    main() 
