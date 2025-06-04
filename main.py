from data_ripper.modules import PswChecker ,EmailChecker
from data_ripper.utils import print_welcome_message
from colorama import Fore, Style

def main():

    print_welcome_message()
    
    print(f""" 
        [{Fore.BLUE}1{Style.RESET_ALL}] Password Checker
        [{Fore.BLUE}2{Style.RESET_ALL}] Email Checker
    """)

    choice = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Select your choice => ")

    if choice == "1":
        psw_to_check = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert password to check => ")
        psw_checker = PswChecker(psw_to_check)
        psw_checker.check_password()
    elif choice == "2":
        email_to_check = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert email to check => ")
        EmailChecker().email_checker_manager(email_to_check)
    else:
        print(f"{Fore.GREEN}[X] Invalid Choice{Style.RESET_ALL}")


if __name__ == "__main__":
    main()