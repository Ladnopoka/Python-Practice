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
    # Convert the number to a list of characters (digits)
    num_list = list(str(num))
    
    # Store the last index of each digit (0-9)
    last = {int(x): i for i, x in enumerate(num_list)}

    # Iterate through the digits
    for i, digit in enumerate(num_list):
        # Check if there's a larger digit later in the list to swap with
        for d in range(9, int(digit), -1):
            if last.get(d, -1) > i:
                # If a larger digit exists and its position is after the current one
                num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                # Return the result after swapping
                return int(''.join(num_list))

    # If no swap improves the number, return the original number
    return num
 
if __name__ == "__main__":
    main() 
