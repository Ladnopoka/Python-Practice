from typing import List

def getWordsInLongestSubsequence(words: List[str], groups: List[int]) -> List[str]:
    if len(words) == 1:
        return [words[0]]

    result = []

    for i in range(len(groups)-1):
        hammer_time = 0
        if len(words[i]) != len(words[i+1]):
            continue

        for chr1, chr2 in zip(words[i], words[i+1]):
            if chr1 != chr2:
                hammer_time += 1

        if groups[i] != groups[i+1] and hammer_time == 1:
            if len(result) == 0:
                result.append(words[i])
            result.append(words[i+1])

    return result
        
# Main function
def main():
    words = ["bdb","aaa","ada"]
    groups = [2,1,3]

    words2 = ["bad","dc","bc","ccd","dd","da","cad","dba","aba"]
    groups2 = [9,7,1,2,6,8,3,7,2]

    print(getWordsInLongestSubsequence(words2, groups2))

# Run the script
if __name__ == "__main__":
    main()