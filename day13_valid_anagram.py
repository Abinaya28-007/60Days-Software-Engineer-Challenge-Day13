def is_anagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}

    # Count characters in first string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract characters using second string
    for char in t:
        if char not in char_count:
            return False

        char_count[char] -= 1

        if char_count[char] < 0:
            return False

    return True


# Examples
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(is_anagram("anagram", "nagaram"))