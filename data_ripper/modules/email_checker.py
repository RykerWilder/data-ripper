import requests
import time
from colorama import Style, Fore

class EmailChecker():
    def __init__(self):
        self.headers = {"User-Agent": "HIBP-Checker-Python"}

    def check_email(self, email):
        api_url = f"https://haveibeenpwned.com/api/v2/breachedaccount/{email}"
        
        try:
            response = requests.get(api_url, headers=self.headers)
            response.raise_for_status()  # HTTP error check
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return []  
            else:
                print(f"{Fore.RED}[X] Error: {response.status_code} - {response.text}{Style.RESET_ALL}")
                return None
        
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[X] Request error: {e}{Style.RESET_ALL}")
            return None

    def email_checker_manager(self, email):
        print(f"{Fore.YELLOW}[!] Checking '{email}'...{Style.RESET_ALL}")

        breaches = self.check_email(email)

        if breaches is None:
            print(f"{Fore.RED}[X] Error during check.{Style.RESET_ALL}")
        elif not breaches:
            print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} No breaches found for this email.")
        else:
            print(f"{Fore.RED}[!] Found {len(breaches)} breach for '{email}':{Style.RESET_ALL}")
            for breach in breaches:
                print(f"\n- Name: {Fore.CYAN}{breach['Name']}{Style.RESET_ALL}")
                print(f"- Title: {breach['Title']}")
                print(f"- BreachDate: {Fore.YELLOW}{breach['BreachDate']}{Style.RESET_ALL}")
                print(f"- Exposed Data: {Fore.MAGENTA}{', '.join(breach['DataClasses'])}{Style.RESET_ALL}")
        
        # timing
        time.sleep(1.5)