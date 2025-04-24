def to_lower(s):
    """Convert string to lowercase without built-in functions"""
    result = []
    for char in s:
        # Check if uppercase (ASCII 65-90)
        if 65 <= ord(char) <= 90:
            result.append(chr(ord(char) + 32))  # Convert to lowercase
        else:
            result.append(char)
    return "".join(result)

def to_upper(s):
    """Convert string to uppercase without built-in functions"""
    result = []
    for char in s:
        # Check if lowercase (ASCII 97-122)
        if 97 <= ord(char) <= 122:
            result.append(chr(ord(char) - 32))  # Convert to uppercase
        else:
            result.append(char)
    return "".join(result)

def toggle_case(s):
    """Toggle case of characters without built-in functions"""
    result = []
    for char in s:
        if 97 <= ord(char) <= 122:  # Lowercase → uppercase
            result.append(chr(ord(char) - 32))
        elif 65 <= ord(char) <= 90:  # Uppercase → lowercase
            result.append(chr(ord(char) + 32))
        else:
            result.append(char)
    return "".join(result)

# Example usage
input_str = "Hello Python!"
print("Lowercase:", to_lower(input_str))  # hello python!
print("Uppercase:", to_upper(input_str))  # HELLO PYTHON!
print("Toggle Case:", toggle_case(input_str))  # hELLO pYTHON!
