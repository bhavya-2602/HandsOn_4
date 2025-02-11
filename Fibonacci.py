# Define the Fibonacci function
def fib(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: sum of the two previous Fibonacci numbers
    return fib(n - 1) + fib(n - 2)

# Main block of code
if __name__ == "__main__":
    n = 5  # Define the number n for which Fibonacci is calculated
    # Print the result of the Fibonacci function for n
    print("Fibonacci of {} is: {}".format(n, fib(n)))
