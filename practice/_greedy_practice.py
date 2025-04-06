def make_change(amount, coins):
    # Sort coins in descending order
    coins.sort(reverse=True)
    
    # Initialize result list to store selected coins
    result = []
    
    # Initialize remaining amount
    remaining = amount
    
    # Try each coin denomination
    for coin in coins:
        # While we can still use the current coin
        while remaining >= coin:
            # Add the coin to our result
            result.append(coin)
            # Subtract the coin value from remaining amount
            remaining -= coin
    
    return result


def partition_palindromes(s):
    result = []
    start = 0
    
    while start < len(s):
        # Try to find the longest palindrome starting at 'start'
        end = len(s) - 1
        while end >= start:
            if is_palindrome(start, end, s):
                result.append(s[start:end + 1])
                break
            end -= 1
        start = end + 1
            
    return result

def is_palindrome(start, end, s):
    # Check if substring from start to end is palindrome
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def main():
    # Example usage
    coins = [25, 10, 5, 1]  # Quarter, dime, nickel, penny
    amount = 67
    change = make_change(amount, coins)
    print(f"To make {amount} cents, use these coins: {change}")


    # Example usage
    test_string = "ababcc"
    partitions = partition_palindromes(test_string)
    print(f"Palindrome partitions of {test_string}: {partitions}")

if __name__ == "__main__":
    main()
