import re

def calculate_password_strength(password):
    # Define the criteria and their corresponding scores
    criteria = [
        (r'.{8,}', "Password length of at least 8 characters", 1),
        (r'[a-z]', "At least one lowercase letter", 1),
        (r'[A-Z]', "At least one uppercase letter", 1),
        (r'\d', "At least one digit", 1),
        (r'[!@#$%^&*(),.?":{}|<>]', "At least one special character", 1),
    ]
    
    # Initialize the strength score
    strength_score = 0
    
    # Check each criterion and update the strength score
    for pattern, description, score in criteria:
        if re.search(pattern, password):
            strength_score += score
    
    # Provide feedback based on the strength score
    if strength_score < 3:
        strength_level = "Weak"
    elif strength_score < 5:
        strength_level = "Moderate"
    else:
        strength_level = "Strong"
    
    # Return the results
    return strength_level, strength_score

def main():
    while True:
        # Ask the user to input a password
        password = input("Enter a password to test its strength (or 'exit' to quit): ")
        
        # Check if the user wants to exit
        if password.lower() == 'exit':
            print("Exiting the Password Strength Tester. Goodbye!")
            break
        
        # Calculate the password strength
        strength_level, strength_score = calculate_password_strength(password)
        
        # Provide feedback to the user
        print(f"Password Strength: {strength_level}")
        print(f"Strength Score: {strength_score}/5")
        
        # Ask if the user wants to enter another password
        continue_testing = input("Do you want to test another password? (yes/no): ").strip().lower()
        if continue_testing != 'yes':
            print("Exiting the Password Strength Tester. Goodbye!")
            break

if __name__ == "__main__":
    main()
