name = input("Enter your full name: ").strip()
parts = name.split()
if len(parts) >= 2:
    first_initial = parts[0][0]
    last_initial = parts[-1][0]
    print(f"Your initials are: {first_initial.upper()}.{last_initial.upper()}")
else:
    print("Please enter both first and last name.")
