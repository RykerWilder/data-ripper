import requests
import time
from colorama import Style, Fore

class EmailChecker():
    def __init__(self, email):
        self.email = email

    def check_email(self, email):
        headers = {"User-Agent": "HIBP-Checker-Python"}
        if api_key:
            headers["hibp-api-key"] = api_key
        
        api_url = f"https://haveibeenpwned.com/api/v2/breachedaccount/{self.email}"
        
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()  # HTTP error check
            
            if response.status_code == 200:
                breaches = response.json()
                return breaches
            elif response.status_code == 404:
                return []  
            else:
                print(f"{Fore.RED}[X]Error: {response.status_code} - {response.text}{Style.RESET_ALL}")
                return None
        
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[X]Request error: {e}{Style.RESET_ALL}")
            return None

    def email_checker_manager(self, email):
        print(f"{Fore.YELLOW}[!]Checking '{email}'...{Style.RESET_ALL}")

        breaches = check_email(email)

        if breaches is None:
            print(f"{Fore.RED}[X]Error during check{Style.RESET_ALL}")
        elif not breaches:
            print("✅ Nessun breach trovato per questa email!")
        else:
            print(f"❌ Trovati {len(breaches)} breach per '{email}':")
            for breach in breaches:
                print(f"\n- Nome: {breach['Name']}")
                print(f"- Titolo: {breach['Title']}")
                print(f"- Data del breach: {breach['BreachDate']}")
                print(f"- Dati esposti: {', '.join(breach['DataClasses'])}")
    
    # Timing
    time.sleep(1.5)