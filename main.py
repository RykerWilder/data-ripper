from data_ripper.modules import PswChecker
import colorama

def main():
    
    print(f""" 
        [{Fore.BLUE}1{Style.RESET_ALL}] Password Checker
    """)

    choice = input(f"{Fore.GREEN}[?] Select your choice => {Style.RESET_ALL}")

    if choice == "1":
        psw_to_check = input(f"{Fore.GREEN}[?] Insert password to check => {Style.RESET_ALL}")
        checker = PswChecker(psw_to_check)
        checker.check_password()
    else:
        print(f"{Fore.GREEN}[X] Invalid Choice{Style.RESET_ALL}")