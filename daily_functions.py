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
def flatten_list(nested: list) -> list:
    return [item for sublist in nested for item in sublist]

def fibonacci(n: int) -> list:
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
def remove_duplicates(lst: list) -> list:
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
def find_max_min(lst: list) -> dict:
    if not lst:
        raise ValueError("List must not be empty.")
    return {"max": max(lst), "min": min(lst)}
if __name__ == "__main__":
    print("=" * 50)
    print("DAY 1 — String Utilities")
    print("=" * 50)
    print("reverse_string('hello')         →", reverse_string("hello"))
    print("is_palindrome('racecar')        →", is_palindrome("racecar"))
    print("count_vowels('hello world')     →", count_vowels("hello world"))
    print("factorial(5)                    →", factorial(5))
    print("fibonacci(7)                    →", fibonacci(7))
    print("flatten_list([[1,2],[3,4]])      →", flatten_list([[1, 2], [3, 4]]))
    print("remove_duplicates([1,2,2,3,1])  →", remove_duplicates([1, 2, 2, 3, 1]))
    print("find_max_min([3,7,1,9,4])       →", find_max_min([3, 7, 1, 9, 4]))
 
 
