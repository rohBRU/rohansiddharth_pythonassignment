password = input("Enter your password: ")
has_letter = any(ch.isalpha() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(ch in "@#$%&" for ch in password)

if len(password) < 6 or (has_letter and not has_digit and not has_special):
    print("Password strength: Weak")
elif len(password) >= 6 and has_letter and has_digit and not has_special:
    print("Password strength: Moderate")
elif len(password) >= 8 and has_letter and has_digit and has_special:
    print("Password strength: Strong")
else:
    print("Password strength: Weak")
