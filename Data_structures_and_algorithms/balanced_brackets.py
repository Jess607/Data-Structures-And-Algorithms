def is_balanced_brackets(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}  # Matching pairs

    for char in s:
        if char in bracket_map.values():  # Opening bracket
            stack.append(char)
        elif char in bracket_map:  # Closing bracket
            if not stack or stack[-1] != bracket_map[char]:  # Mismatch or empty stack
                return "NO"
            stack.pop()  # Remove matched opening bracket
    
    return "YES" if not stack else "NO"