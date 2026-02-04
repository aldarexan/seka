# ============================================
# BASIC STRING METHODS AND OPERATIONS IN PYTHON
# ============================================

# 1. STRING CREATION
print("=" * 50)
print("1. STRING CREATION")
print("=" * 50)
text = "Hello, Python World!"
multi_line = """This is a
multi-line string"""
print(f"Single line: {text}")
print(f"Multi-line: {multi_line}\n")

# 2. CASE CONVERSION
print("=" * 50)
print("2. CASE CONVERSION")
print("=" * 50)
sample = "Python Programming"
print(f"Original: {sample}")
print(f"Upper: {sample.upper()}")
print(f"Lower: {sample.lower()}")
print(f"Title: {sample.title()}")
print(f"Capitalize: {sample.capitalize()}")
print(f"Swap case: {sample.swapcase()}\n")

# 3. STRING SEARCHING
print("=" * 50)
print("3. STRING SEARCHING")
print("=" * 50)
text = "Learning Python is fun and Python is powerful"
print(f"Text: {text}")
print(f"Find 'Python': {text.find('Python')}")
print(f"Count 'Python': {text.count('Python')}")
print(f"Starts with 'Learning': {text.startswith('Learning')}")
print(f"Ends with 'powerful': {text.endswith('powerful')}\n")

# 4. STRING MODIFICATION
print("=" * 50)
print("4. STRING MODIFICATION")
print("=" * 50)
text = "  Hello World  "
print(f"Original: '{text}'")
print(f"Strip: '{text.strip()}'")
print(f"Replace: '{text.replace('World', 'Python')}'")
print(f"Remove 'Hello': '{text.replace('Hello', '')}')\n")

# 5. STRING SPLITTING AND JOINING
print("=" * 50)
print("5. SPLITTING AND JOINING")
print("=" * 50)
sentence = "Python,Java,JavaScript,C++"
print(f"Original: {sentence}")
words = sentence.split(',')
print(f"Split by comma: {words}")
joined = " | ".join(words)
print(f"Join with ' | ': {joined}\n")

# 6. STRING FORMATTING
print("=" * 50)
print("6. STRING FORMATTING")
print("=" * 50)
name = "Alice"
age = 25
# f-strings (Python 3.6+)
print(f"f-string: My name is {name} and I'm {age} years old")
# format() method
print("format(): My name is {} and I'm {} years old".format(name, age))
# % formatting (old style)
print("% formatting: My name is %s and I'm %d years old" % (name, age))
print()

# 7. STRING CHECKING METHODS
print("=" * 50)
print("7. STRING CHECKING METHODS")
print("=" * 50)
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"'   '.isspace(): {'   '.isspace()}")
print(f"'Hello World'.istitle(): {'Hello World'.istitle()}\n")

# 8. STRING SLICING
print("=" * 50)
print("8. STRING SLICING")
print("=" * 50)
text = "Python Programming"
print(f"Original: {text}")
print(f"First 6 chars: {text[:6]}")
print(f"Last 11 chars: {text[-11:]}")
print(f"Every 2nd char: {text[::2]}")
print(f"Reverse: {text[::-1]}\n")

# 9. STRING CONCATENATION
print("=" * 50)
print("9. STRING CONCATENATION")
print("=" * 50)
first = "Hello"
second = "World"
print(f"Using +: {first + ' ' + second}")
print(f"Using *: {first * 3}")
print(f"Using join: {' '.join([first, second])}\n")

# 10. STRING LENGTH AND INDEXING
print("=" * 50)
print("10. LENGTH AND INDEXING")
print("=" * 50)
text = "Python"
print(f"Text: {text}")
print(f"Length: {len(text)}")
print(f"First character: {text}")
print(f"Last character: {text[-1]}")
print(f"Character at index 2: {text}\n")

print("=" * 50)
print("DEMO COMPLETE!")
print("=" * 50)