from typing import List

def count_ways(n):
    def backtrack(position, path):
        if position == n:
            print(path)
            return
        elif position > n:
            return
        
        backtrack(position + 1, path + [0])
        if len(path) == 0 or path[-1] == 0:
            backtrack(position + 1, path + [1]) 
        
    backtrack(0, [])
        
# Main function
def main():
    n = 3

    count_ways(n)

# Run the script
if __name__ == "__main__":
    main()