import re

def assess_password_strength(password):
    feedback = []
    
    # Criteria checks
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Count how many criteria are met
    score = sum([length_criteria, upper_criteria, lower_criteria, number_criteria, special_criteria])
    
    # Feedback for each unmet criterion
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_criteria:
        feedback.append("Password should include at least one special character.")
    
    # Determine strength
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    elif score == 3:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return strength, feedback

if __name__ == "__main__":
    while True:
        password = input("Enter a password to assess (or 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Exiting the password strength checker.")
            break
        
        strength, feedback = assess_password_strength(password)
        print(f"\nPassword strength: {strength}")
        
        if feedback:
            print("Suggestions to improve your password:")
            for comment in feedback:
                print(f"- {comment}")
        else:
            print("Your password is strong!")
        
        print("\n" + "="*50 + "\n")
