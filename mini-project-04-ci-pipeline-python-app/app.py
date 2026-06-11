def check_length(password):
    return len(password) >= 8


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def has_digit(password):
    return any(char.isdigit() for char in password)


def password_strength(password):
    if not password:
        raise ValueError("Password cannot be empty")

    score = 0

    if check_length(password):
        score += 1
    if has_uppercase(password):
        score += 1
    if has_lowercase(password):
        score += 1
    if has_digit(password):
        score += 1

    if score == 4:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"


if __name__ == "__main__":
    pwd = "Test1234"
    print("Password Strength Checker")
    print(f"Password: {pwd}")
    print(f"Strength: {password_strength(pwd)}")
