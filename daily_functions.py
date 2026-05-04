def reverse_string(s: str) -> str:
    return s[::-1]
def is_prime(n: int) -> bool:
    """
    Checks whether a number is prime.
 
    Args:
        n (int): The number to check.
 
    Returns:
        bool: True if prime, False otherwise.
 
    Example:
        >>> is_prime(17)
        True
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True




if __name__ == "__main__":
    print("=" * 50)
    print("DAY 1 — String Utilities")
    print("=" * 50)
    print("reverse_string('helloow')         →", reverse_string("hello"))
