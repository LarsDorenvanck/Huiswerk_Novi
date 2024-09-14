import re

# Example of reading a Python file (assuming 'your_file.py' contains Python code)
with open('loops.py', 'r') as file:
    code = file.read()

# Remove all comments using the regex
clean_code = re.sub(r"#.*|'''[\s\S]*?'''|\"\"\"[\s\S]*?\"\"\"", '', code)

# Save the cleaned code to a new file or print it
with open('cleaned_file.py', 'w') as file:
    file.write(clean_code)
