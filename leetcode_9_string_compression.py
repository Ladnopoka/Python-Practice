def main():
    nums = [3,2,2,3]
    nums1 = [0,1,2,2,3,0,4,2]
    val = 3
    val1 = 2
    str1 = "abcde"
    str2 = "bbbbbbuuuuuuuuuvvvssssssssssppppppppppwwwwwwwwwttn"

    print(compressedString(str2))

def compressedString(word: str) -> str:
    if len(word) == 1:
        return str(1) + word

    comp = ""
    comp_array = []
    counter_char = 1
    current_char = word[0]

    for i in range(1, len(word)):
        if counter_char == 9:
            comp_array.append(counter_char)
            comp_array.append(current_char)
            counter_char = 1
        else:
            if current_char == word[i]:
                counter_char += 1
            else:
                comp_array.append(counter_char)
                comp_array.append(current_char)
                current_char = word[i]
                counter_char = 1

        if i == len(word)-1:
            current_char = word[i]
            comp_array.append(counter_char)
            comp_array.append(current_char)
            current_char = word[i]
            counter_char = 1

    comp = ''.join(map(str, comp_array))

    return comp

if __name__ == "__main__":
    main() 


        def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []
        result = []
        current = p

        while current or stack:
            while current:
                print(current.val)
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            
            current = current.right

        print("Result: ", result)

        return result
        