def main():
    result = romanToInt("MCMXCIV")

    print(result)
    
def romanToInt(s) -> int:
        roman_map = {
            1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 
            4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"
        }
        
        roman_num = 0
        i = 0
        n = len(s)

        while i < n:
            if i < n - 1 and s[i:i+2] in roman_map.values():
                for num, roman_char in roman_map.items():
                    if s[i:i+2] == roman_char:
                        print(f"Matched {roman_char} with value {num}")
                        roman_num += num
                        i += 2
                        break
            else:
                if s[i] in roman_map.values():
                    for num, roman_char in roman_map.items():
                        if s[i] == roman_char:
                            print(f"Matched {roman_char} with value {num}")
                            roman_num += num
                            i += 1
                            break

        return roman_num

if __name__ == "__main__":
    main()  # Run the main function