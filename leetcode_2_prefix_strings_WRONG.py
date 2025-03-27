from collections import defaultdict, Counter

def main():
    str = ["dog","racecar","car"]
    str2 = ["flower","flow","flight"]
    str3 = ["aton","agon","abon"]
    str4 = ["a"]
    result = longestCommonPrefix(str)

    print(result)

def longestCommonPrefix(strs) -> str:
        if len(strs) == 1:
            return strs[0]
        
        prefix_map = defaultdict(Counter)
        strs.sort()

        result_string = ""
        max_count = 0

        for string in strs:
            if len(string) < 1:
                continue
            else:
                for num, char in enumerate(string):
                    prefix_map[num][char] += 1

        if prefix_map:
            if min(prefix_map[0].values()) < 2:
                return ""
            else:
                max_count = max(prefix_map[0].values())

                for index, counter in prefix_map.items():
                    print("Index: ", index, "Counter: ", counter)

                    for char, count in counter.items():
                        if count < max_count:
                            return result_string
                        
                        if count == max_count:
                            result_string = result_string + char

        return result_string


if __name__ == "__main__":
    main()  # Run the main function 
