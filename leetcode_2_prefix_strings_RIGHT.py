def main():
    str = ["dog","racecar","car"]
    str2 = ["flower","flow","flight"]
    str3 = ["aton","agon","abon"]
    str4 = ["a"]
    str5 = ["abab","aba",""]
    str6 = ["ab","caca","accc","cbcb"]
    result = longestCommonPrefix(str6)

    print(result)    

def longestCommonPrefix(strs) -> str:
    if len(strs) == 1:
        return strs[0]
    
    if "" in strs:
        return ""

    for index in range(len(strs[0])):
        char = strs[0][index]

        for string in strs:
            if index >= len(string) or string[index] != char:
                return string[:index] 

    return strs[0]

if __name__ == "__main__":
    main()  # Run the main function 
