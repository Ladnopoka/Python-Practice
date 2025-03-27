
def main():
    str = ["dog","racecar","car"]
    str2 = ["flower","flow","flight"]
    str3 = ["aton","agon","abon"]
    str4 = ["a"]
    str5 = ["abab","aba",""]
    str6 = [0,0,1,1,1,2,2,3,3,4]
    str7 = [1,2]

    num1 = 7
    num2 = 1
    num3 = 0

    print(longestDiverseString(num1, num2, num3))

def longestDiverseString(a: int, b: int, c: int) -> str:
    if max(a,b,c) < 1:
        return ""

    counts = [('a', a), ('b', b), ('c', c)]
    last_char = ''
    last_char_number = 0
    
    result = []
    
    while any(count > 0 for char, count in counts):
        counts.sort(key=lambda x: -x[1])

        added = False
        
        for i, (char, count) in enumerate(counts):
            if count > 0 and not (char == last_char and last_char_number == 2):
                result.append(char)
                last_char_number = last_char_number + 1 if char == last_char else 1
                last_char = char
                counts[i] = (char, count - 1)
                added = True
                break

        if not added:
            break

    return ''.join(result)
    
if __name__ == "__main__":
    main() 
