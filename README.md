# Password Strength Assessor

This Python script assesses the strength of a given password based on various criteria including length, complexity, and the presence of personal information or common patterns.

## Usage

1. **Requirements:** Ensure you have Python installed on your system.
2. **Clone the Repository:** Clone this repository to your local machine.
3. **Run the Script:**
    ```bash
    python assess_password_strength.py
    ```
4. **Follow the Prompts:** Enter your password when prompted.
5. **Review Feedback:** The script will provide feedback on the strength of your password.

## Functionality

The script checks the following criteria for password strength:

- **Length Requirement:** Password must be at least 12 characters long.
- **Case Sensitivity:** Password must contain both upper and lower case letters.
- **Inclusion of Numerical Digits:** Password must include one or more numerical digits.
- **Inclusion of Special Characters:** Password must include special characters.
- **Prohibited Passwords:**
  - Cannot be entirely numeric or alphabetic.
  - Cannot contain repetitive characters.
  - Cannot contain common words found in the blocklist.
  - Cannot contain personal information.
  - Cannot contain the company name or abbreviation.
- **Prohibition of Common Numbers Format:** Password cannot match the format of calendar dates, license plate numbers, or telephone numbers.
- **Combination of Words, Special Characters, and Numbers:** Password must contain a combination of words, special characters, and numbers.

## Customization

You can customize the script by adjusting the following parameters:

- `personal_info`: List of personal information to check against (e.g., name, birth year).
- `blocklist`: List of common passwords or words to block.
- `company_name`: Name of the company to avoid in passwords.

