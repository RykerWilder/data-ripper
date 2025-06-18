import requests
import hashlib
from colorama import Fore, Style

class PswChecker:
    def __init__(self, password):
        self.password = password

    def check_password(self):
        if not self.password:
            print(f"{Fore.RED}[X] Password cannot be empty.{Style.RESET_ALL}")
            return

        sha1_password = hashlib.sha1(self.password.encode('utf-8')).hexdigest().upper()
        prefix, suffix = sha1_password[:5], sha1_password[5:]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"{Fore.RED}[X] Error: Could not check password.{Style.RESET_ALL}")
                return

            for line in response.text.splitlines():
                if line.startswith(suffix):
                    count = int(line.split(':')[1])
                    print(f"{Fore.RED}[!]{Style.RESET_ALL} Password compromised! Found in {Fore.RED}{count}{Style.RESET_ALL} breaches.")
                    return
            print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Strong password, not found in known breaches.")

        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[X] Error: {e}{Style.RESET_ALL}")