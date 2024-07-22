import re

def password_strength(password):
    # Define the criteria for password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W]', password) is not None

    # Check how many criteria are met
    criteria_met = [length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_criteria]
    strength = sum(criteria_met)

    # Determine the strength level
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    elif strength == 2:
        return "Weak"
    else:
        return "Very Weak"

def main():
    # Get password input from the user
    password = input("Enter your password to check its strength: ")
    
    # Evaluate the strength of the password
    strength = password_strength(password)
    
    # Print the result
    print(f"Your password strength is: {strength}")

if __name__ == "__main__":
    main()