from typing import List
        
# Main function
def main():
    def fibonaci(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibonaci(num-1) + fibonaci(num-2)

    for i in range(10):
        print(fibonaci(i))

# Run the script
if __name__ == "__main__":
    main()