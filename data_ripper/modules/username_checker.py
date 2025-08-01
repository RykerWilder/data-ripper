import requests
from colorama import Fore, Style
from bs4 import BeautifulSoup
import os

class UsernameChecker:
    def __init__(self):
        self.platforms = {
            'github': {
                'url': 'https://github.com/{}',
                'error': 'Not Found'
            },
            'twitter': {
                'url': 'https://twitter.com/{}',
                'error': 'Page doesn’t exist'
            },
            'instagram': {
                'url': 'https://instagram.com/{}',
                'error': 'Sorry, this page isn\'t available.'
            },
            'facebook': {
                'url': 'https://facebook.com/{}',
                'error': 'This page isn\'t available'
            },
            'reddit': {
                'url': 'https://reddit.com/user/{}',
                'error': 'Sorry, nobody on Reddit goes by that name'
            },
            'pinterest': {
                'url': 'https://pinterest.com/{}',
                'error': 'Sorry, we couldn\'t find that page'
            }
        }
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def check_username_all_platforms(self, username):
        
        # Restituisce una struttura vuota per ogni piattaforma
        results = {}
        for platform in self.platforms:
            results[platform] = {
                'status': 'success',
                'exists': False,
                'platform': platform,
                'username': username,
                'url': self.platforms[platform]['url'].format(username)
            }
        return results

    def check_usernames_from_file(self, file_path):
        if not os.path.exists(file_path):
            return {'status': 'error', 'message': 'File non trovato'}
        
        results = {}
        try:
            with open(file_path, 'r') as file:
                usernames = [line.strip() for line in file.readlines() if line.strip()]
            
            for username in usernames:
                results[username] = self.check_username_all_platforms(username)
            
            return {'status': 'success', 'results': results}
        
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def save_results_to_file(self, results, output_file):
        try:
            with open(output_file, 'w') as file:
                if isinstance(results, dict):
                    if 'results' in results:
                        for username, platforms in results['results'].items():
                            file.write(f"Username: {username}\n")
                            for platform, data in platforms.items():
                                exists = "Esiste" if data.get('exists') else "Non esiste"
                                file.write(f"  {platform.capitalize()}: {exists}\n")
                                if data.get('url'):
                                    file.write(f"    URL: {data['url']}\n")
                            file.write("\n")
                    else:
                        for platform, data in results.items():
                            exists = "Exists" if data.get('exists') else "Non esiste"
                            file.write(f"{platform.capitalize()}: {exists}\n")
                            if data.get('url'):
                                file.write(f"  URL: {data['url']}\n")
            return {'status': 'success', 'message': f'Risultati salvati in {output_file}'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def username_checker_manager(self):
        default_file = "username.txt"
        
        # Cerca automaticamente il file username.txt
        if os.path.exists(default_file):
            print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Found file {default_file}, proceeding with the verification...")
            file_results = self.check_usernames_from_file(default_file)
            if file_results['status'] == 'success':
                self.save_results_to_file(file_results, "username_results.txt")
                print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Verification completed. Results saved in 'username_results.txt'")
            else:
                print(f"{Fore.RED}[X] Error processing file: {file_results['message']}")
        else:
            # Se il file non esiste, chiedi un username manuale
            print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} File {default_file} not found in the current directory")
            username = input(f"{Fore.GREEN}[?]{Style.RESET_ALL} Insert username to check => ").strip()
            if username:
                results = self.check_username_all_platforms(username)
                self.save_results_to_file(results, "username_results.txt")
                print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Results saved in 'username_results.txt'")
            else:
                print(f"{Fore.RED}[X] No username entered")