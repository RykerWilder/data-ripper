import requests
import hashlib

class PswChecker:
    def __init__(self, password):
        self.password = password

    def check_password(self):
        if not self.password:
            print("Password cannot be empty!")
            return

        sha1_password = hashlib.sha1(self.password.encode('utf-8')).hexdigest().upper()
        prefix, suffix = sha1_password[:5], sha1_password[5:]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        try:
            response = requests.get(url)
            if response.status_code != 200:
                print("Error: Could not check password.")
                return

            for line in response.text.splitlines():
                if line.startswith(suffix):
                    count = int(line.split(':')[1])
                    print(f"⚠️ Password compromised! Found in {count} breaches.")
                    return
            print("✅ Strong password, not found in known breaches.")

        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to connect to the API. {e}")