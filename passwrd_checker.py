import re

def assess_password_strength(password, personal_info=[], blocklist=[], company_name=""):
    # Checklist to track missing criteria
    missing_checklist = []

    # Length Requirement
    if len(password) < 12:
        missing_checklist.append("Password must be at least 12 characters long.")

    # Case Sensitivity
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        missing_checklist.append("Password must contain both upper and lower case letters.")

    # Inclusion of Numerical Digits
    if not any(char.isdigit() for char in password):
        missing_checklist.append("Password must include one or more numerical digits.")

    # Inclusion of Special Characters
    if not any(char in "!@#$%^&*()-_=+[{]};:'\"<,>.?/\\|`~" for char in password):
        missing_checklist.append("Password must include special characters.")

    # Prohibited Passwords
    if password.isdigit() or password.isalpha():
        missing_checklist.append("Password cannot be entirely numeric or alphabetic.")
    if re.search(r'(.)\1{2,}', password):
        missing_checklist.append("Password cannot contain repetitive characters.")
    if any(word in password.lower() for word in blocklist):
        missing_checklist.append("Password cannot contain common words found in the blocklist.")
    if any(info.lower() in password.lower() for info in personal_info):
        missing_checklist.append("Password cannot contain personal information.")
    if company_name.lower() in password.lower() or company_name.lower().replace(" ", "") in password.lower():
        missing_checklist.append("Password cannot contain the company name or abbreviation.")

    # Prohibition of Common Numbers Format
    if re.search(r'\b(?:19|20)\d{2}\b', password) or re.search(r'\b\d{2}[.-]?\d{2}[.-]?\d{2,4}\b', password):
        missing_checklist.append("Password cannot match the format of calendar dates, license plate numbers, or telephone numbers.")

    # Ensure the presence of a combination of words, special characters, and numbers
    if not (any(char.isalpha() for char in password) and any(char.isdigit() for char in password) and any(char in "!@#$%^&*()-_=+[{]};:'\"<,>.?/\\|`~" for char in password)):
        missing_checklist.append("Password must contain a combination of words, special characters, and numbers.")

    # If all criteria are met
    if not missing_checklist:
        return "Password meets complexity requirements."
    else:
        return "\n".join(missing_checklist)

# Example usage:
password = input("Enter your password: ")
# Example personal info and blocklist
personal_info = ["john", "doe", "1985"]
blocklist = ["password", "qwerty", "123456"]
company_name = "example company"
strength_feedback = assess_password_strength(password, personal_info, blocklist, company_name)
print(strength_feedback)

