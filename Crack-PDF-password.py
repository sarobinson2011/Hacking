# Import Required Module
import pikepdf
from tqdm import tqdm

# Empty password list
passwords = []

# Contain passwords in text file
# password_text_file = "/home/oem/Documents/wordlist.txt"

# Iterate through each line
# and store in passwords list
for line in open("/home/oem/Documents/wordlist.txt"):
    passwords.append(line.strip())

# iterate over passwords
for password in tqdm(passwords, "Attempting to brute force attack PDF password"):
    try:

        # open PDF file and check each password in turn
        with pikepdf.open("/home/oem/Documents/Quotes.pdf", password=password) as p:
            # If password is correct, break the loop
            print("[+] Password found:", password)
            break

    # If password does not match, it will raise PasswordError
    except pikepdf._qpdf.PasswordError as e:
        # if password is wrong, continue the loop
        continue
