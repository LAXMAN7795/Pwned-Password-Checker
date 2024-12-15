import requests  # Importing the requests module to make HTTP requests
import hashlib  # Importing hashlib for generating SHA1 hashes

def request_api(query_char):
    """
    Function to send a request to the Pwned Passwords API with the first 5 characters of a SHA1 hash.
    :param query_char: First 5 characters of the SHA1 hash.
    :return: Response object from the API.
    """
    url = 'https://api.pwnedpasswords.com/range/' + query_char  # Constructing the API URL
    response1 = requests.get(url)  # Sending a GET request to the API
    
    # Checking if the response status is not OK (200)
    if response1.status_code != 200:
        raise RuntimeError(f"Error fetching: RX{response1.status_code}, please check the API and try again.")
    return response1  # Returning the API response

def get_password_leaks_count(hashes, hash_to_check):
    """
    Function to check how many times a password hash appears in the API response.
    :param hashes: The response text containing hashes and counts.
    :param hash_to_check: The tail of the SHA1 hash to look for.
    :return: The count of occurrences of the hash.
    """
    # Splitting each line into hash and count, creating a generator object
    hashes = (line.split(':') for line in hashes.text.splitlines())
    
    for h, count in hashes:  # Iterating through all hash-count pairs
        if h == hash_to_check:  # If the hash matches the tail of the given hash
            return count  # Return the count
    return 0  # Return 0 if the hash is not found

def pwned_api_check(password):
    """
    Function to check if a password has been leaked using the Pwned Passwords API.
    :param password: The password to check.
    :return: The count of times the password was found.
    """
    # Converting the password to a SHA1 hash and converting it to uppercase
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # Splitting the hash into the first 5 characters and the rest
    first_five_char, tail = sha1password[:5], sha1password[5:]
    
    # Requesting the API with the first 5 characters of the hash
    response2 = request_api(first_five_char)
    
    # Checking how many times the tail appears in the response
    return get_password_leaks_count(response2, tail)

def main(args):
    """
    Main function to process a list of passwords and check them against the API.
    :param args: List of passwords to check.
    """
    for password in args:  # Iterating through each password in the list
        count = pwned_api_check(password)  # Checking the password using the API
        
        # Printing the result based on the count of leaks
        if count:
            print(f"{password} found {count} times, you should probably change the password.")
        else:
            print(f"{password} was NOT found, you can carry on.")
    
    print("Done!")  # Indicating the process is complete

def user_input(n):
    """
    Function to take user input for a specified number of passwords.
    :param n: Number of passwords to input.
    :return: Calls the main function with the list of passwords.
    """
    password_list = []  # List to store user-provided passwords
    
    for i in range(n):  # Loop to collect 'n' passwords
        password = input("Enter your password: ")  # Prompting the user for a password
        password_list.append(password)  # Adding the password to the list
    
    return main(password_list)  # Calling the main function with the password list

if __name__ == '__main__':
    """
    Entry point of the script. Takes user input for the number of passwords to check.
    """
    num = int(input("Enter how many passwords you want to check: "))  # Asking for the number of passwords
    user_input(num)  # Calling the user_input function with the given number
