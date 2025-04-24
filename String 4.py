def remove_substring(main_str, remove_str):
    """Remove all occurrences of `remove_str` from `main_str`"""
    return main_str.replace(remove_str, "")

# Example usage
original = "abcdef"
removed = remove_substring(original, "cd")
print(f"Original: {original} → Modified: {removed}")  # Output: abef
