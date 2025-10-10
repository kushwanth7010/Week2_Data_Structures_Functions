# Working with Lists, Tuples, Sets, Dictionaries, and Functions

# Sum of squares using list comprehension
def sum_of_squares(numbers):
    return sum([n**2 for n in numbers])

# Filter even numbers using lambda
def filter_even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

# Recursion example - factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    print("Numbers:", nums)
    print("Sum of Squares:", sum_of_squares(nums))
    print("Even Numbers:", filter_even(nums))
    print("Factorial of 5:", factorial(5))
