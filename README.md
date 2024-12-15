# Pwned Password Checker

This project is a Python-based application that checks if your passwords have been leaked using the [Pwned Passwords API](https://haveibeenpwned.com/API/v3#PwnedPasswords). It allows users to input passwords and checks them securely by using the k-anonymity model to protect the full password from being exposed.

## Features

- **Secure Password Checking**: Utilizes SHA-1 hashing and the first 5 characters of the hash to query the API, ensuring privacy.
- **API Integration**: Checks passwords against a database of leaked credentials using the Pwned Passwords API.
- **Interactive User Input**: Allows users to input multiple passwords to check in a single session.
- **Clear Feedback**: Provides a count of how many times a password has been found in breaches or confirms that the password has not been found.
- **Ease of Use**: A simple command-line interface for seamless interaction.
- **Hover Effects**: Highlights key processes in code comments for better understanding.
- **Error Handling**: Gracefully handles API errors and unexpected inputs.

## Installation

1. Clone the repository to your local machine:
   git clone https://github.com/yourusername/pwned-password-checker.git
   cd pwned-password-checker

2. Ensure you have Python 3 installed on your system.

3. Install the required dependencies (if any). This project uses the `requests` library:
   pip install requests

## Usage

1. Run the script:
   python pwned_password_checker.py

2. Input the number of passwords you want to check:
   Enter how many passwords you want to check: 2

3. Enter each password when prompted:
   Enter your password: password123
   Enter your password: mysecurepassword

4. The script will output results for each password:
   password123 found 2304 times, you should probably change the password.
   mysecurepassword was NOT found, you can carry on.
   Done!

## How It Works

1. **SHA-1 Hashing**: Each password is hashed using SHA-1 and converted to uppercase.
2. **k-Anonymity Query**: The first 5 characters of the hash are sent to the API to fetch possible matches.
3. **Match Checking**: The script checks the returned hashes for a match with the remaining part of the hash and retrieves the count of breaches.
4. **User-Friendly Feedback**: Results are displayed in an easy-to-read format, guiding users to take appropriate actions.

## Security

- This tool never sends your full password to the API.
- It uses the k-anonymity model to ensure that your data remains secure.
- Passwords are hashed locally before querying the API, protecting sensitive information.

## Example Output

Enter how many passwords you want to check: 1
Enter your password: password123
password123 found 2304 times, you should probably change the password.
Done!

## Requirements

- Python 3.x
- `requests` library

Install `requests` using pip:
pip install requests

## Error Handling

- If the API request fails (non-200 status code), a descriptive error message is raised.
- Invalid inputs are handled gracefully to ensure the program runs smoothly.

## Contributing

Feel free to submit issues or pull requests to improve this project. Contributions are welcome!

## Future Improvements

- **GUI Integration**: Add a graphical interface for non-technical users.
- **Expanded Functionality**: Include additional checks for email addresses and usernames.
- **Logging**: Provide an option to log results for future reference.
- **Multithreading**: Improve performance when checking multiple passwords.
