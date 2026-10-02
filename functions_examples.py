# Working with Lists, Tuples, Sets, Dictionaries, and Functions

def sum_of_squares(numbers):
    """Return the sum of the squares of the input numbers."""
    return sum(n ** 2 for n in numbers)


def filter_even(numbers):
    """Return the even integers from the input iterable."""
    return [x for x in numbers if x % 2 == 0]


def factorial(n):
    """Return n!, rejecting negative or non-integral inputs."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("factorial requires a non-negative integer")
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    print("Numbers:", nums)
    print("Sum of Squares:", sum_of_squares(nums))
    print("Even Numbers:", filter_even(nums))
    print("Factorial of 5:", factorial(5))
