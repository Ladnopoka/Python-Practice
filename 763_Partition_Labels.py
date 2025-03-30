def partitionLabels(s):
    result = []
    partition_start = 0
    last_char = {}
    max_end_position = -1

    for i in range(len(s)):
        last_char[s[i]] = i

    for i in range(len(s)):
        if last_char[s[i]] > max_end_position:
            max_end_position = last_char[s[i]]

        if i == max_end_position:
            result.append(max_end_position - partition_start + 1)
            partition_start = i + 1

    return result

def main():
    s = "ababcc"
    s2 = "eccbbbbdec"
    s3 = "ababcbacadefegdehijhklij"
    print("First: ", partitionLabels(s))
    print("Second: ", partitionLabels(s2))
    print("Third: ", partitionLabels(s3))

if __name__ == "__main__":
    main()