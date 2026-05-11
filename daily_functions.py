def reverse_string(s: str) -> str:
    return s[::-1]
def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
def count_vowels(s: str) -> int:
    return sum(1 for ch in s.lower() if ch in "aeiou")

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("=" * 50)
    print("DAY 1 — String Utilities")
    print("=" * 50)
    print("reverse_string('hello')         →", reverse_string("hello"))
    print("is_palindrome('racecar')        →", is_palindrome("racecar"))
    print("count_vowels('hello world')     →", count_vowels("hello world"))
    print("factorial(5)                    →", factorial(5))
