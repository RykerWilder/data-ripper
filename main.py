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
            domain_to_check = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert username to check => ")
            checker = UsernameChecker()
            # Verifica username
            results_all = checker.check_username_all_platforms("mario_rossi")
            print(results_all)
            # Salva i risultati in un file
            checker.save_results_to_file(results_all, "risultati_username.txt")
            # Verifica una lista di username da file
            print("\nVerifica da file:")
            file_results = checker.check_usernames_from_file("usernames.txt")
            if file_results['status'] == 'success':
                checker.save_results_to_file(file_results, "risultati_multipli.txt")
                print(file_results.get('message', 'Operazione completata'))
        else:
            print(f"{Fore.RED}[X] Invalid Choice{Style.RESET_ALL}")


if __name__ == "__main__":
    main()