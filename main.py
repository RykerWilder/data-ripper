from data_ripper.modules import PswChecker ,EmailChecker, GetDomainInfo, UsernameChecker
from data_ripper.utils import print_welcome_message, exit
from colorama import Fore, Style
import signal
from getpass import getpass

def main():
    
    # ctrl+c handler
    signal.signal(signal.SIGINT, exit)

    print_welcome_message()
    
    while True:
        print(f""" 
            [{Fore.BLUE}1{Style.RESET_ALL}] Password checker
            [{Fore.BLUE}2{Style.RESET_ALL}] Email checker
            [{Fore.BLUE}3{Style.RESET_ALL}] Get info about domain
            [{Fore.BLUE}4{Style.RESET_ALL}] Username checker
        """)

        choice = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Select your choice => ")

        if choice == "1":
            psw_to_check = getpass(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert password to check => ")
            psw_checker = PswChecker(psw_to_check)
            psw_checker.check_password()
        elif choice == "2":
            email_to_check = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert email to check => ")
            EmailChecker().email_checker_manager(email_to_check)
        elif choice == "3":
            domain_to_check = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert domain to check => ")
            GetDomainInfo().domain_info_manager(domain_to_check)
        elif choice == "4":
            usr_checker = UsernameChecker()
            usr_checker.username_checker_manager()
        else:
            print(f"{Fore.RED}[X] Invalid Choice{Style.RESET_ALL}")


if __name__ == "__main__":
    main()