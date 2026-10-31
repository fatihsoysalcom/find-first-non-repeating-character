import collections

def find_first_non_repeating(s: str) -> str | None:
    """
    Finds the first non-repeating character in a given string.
    This is a classic Dev Challenge problem to test algorithmic thinking and data structure usage.
    """
    if not s:
        return None

    # Step 1: Count character frequencies while preserving insertion order.
    # Using an OrderedDict helps in identifying the 'first' non-repeating character
    # by maintaining the order of character appearance in the string.
    char_counts = collections.OrderedDict()
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Step 2: Iterate through the ordered counts to find the first character with a count of 1.
    # This step directly leverages the preserved order to meet the "first" requirement.
    for char, count in char_counts.items():
        if count == 1:
            # This character appeared only once and is the first one encountered in order.
            return char

    # If no non-repeating character is found after checking all unique characters.
    return None

# --- Demonstration of the Dev Challenge solution ---
if __name__ == "__main__":
    test_strings = [
        "swiss",
        "aabbccdeeff",
        "hello",
        "programming",
        "level",
        "",
        "aaaaa",
        "a",
        "abacaba"
    ]

    print("--- Dev Challenge: Find First Non-Repeating Character ---")
    print("This example demonstrates a common technical challenge problem.")
    print("It highlights algorithmic thinking, data structure usage, and problem-solving skills.")
    print("-" * 60)

    for test_str in test_strings:
        result = find_first_non_repeating(test_str)
        if result:
            print(f"String: '{test_str}' -> First non-repeating character: '{result}'")
        else:
            print(f"String: '{test_str}' -> No non-repeating character found.")
    print("-" * 60)

    print("\nKey skills demonstrated, as often evaluated in Dev Challenges:")
    print("- Algorithmic thinking: Breaking down the problem into frequency counting and ordered iteration.")
    print("- Data structures: Efficient use of `collections.OrderedDict` to maintain insertion order.")
    print("- Problem-solving: Handling edge cases like empty strings or strings with all repeating characters.")
