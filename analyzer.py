
'''Educational tool that analyzes password strength based on security best practices.
Designed for learning defensive cybersecurity concepts.'''

# receive a password
# check it's strength
# return feedback weak/medium/strong
#tell why 


# Length 8< weak / 8-11 medium / 12+ strong / aA23@*&...




allowed_special_chars = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '_', '-', '+', '=', '[', ']',
    '{', '}', '|', '\\', ':', ';', '"', "'",
    '<', '>', ',', '.', '?', '/'
]
password = input("Enter your password: ")

def check_length(password):
    if len(password) >= 12:
        return True
    else:
        return False

def check_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    else:
        return False
    
def check_lowercase(password):
    for char in password:
        if char.islower():
            return True
    else:
        return False
    
def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    else:
        return False
    
def check_special_char(password):
    for char in password:
        if char in allowed_special_chars:
            return True
    else:
        return False

def analyze_password(password):
    checks = [
        check_length,
        check_uppercase,
        check_lowercase,
        check_digit,
        check_special_char
    ]

    score = 0

    for check in checks:
        if check(password):
            score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

result = analyze_password(password)

print(f"Your password is {result}")