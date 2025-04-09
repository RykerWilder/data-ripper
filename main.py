import requests
import hashlib

def check_password(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    for line in response.text.splitlines():
        if suffix in line:
            count = int(line.split(':')[1])
            print(f"Password Compromised! Found in {count} breaches.")
            return
    print("Strong password, not found in known breaches.")

if __name__ == "__main__":
    password = input("Enter the password to verify: ")
    check_password(password)