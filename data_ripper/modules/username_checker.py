import requests
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
        
        # Headers per simulare un browser
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def check_username(self, username, platform):
        """Verifica se un username esiste su una specifica piattaforma"""
        if platform not in self.platforms:
            return {'status': 'error', 'message': f'Piattaforma {platform} non supportata'}
        
        url = self.platforms[platform]['url'].format(username)
        try:
            response = requests.get(url, headers=self.headers)
            content = response.text
            
            if response.status_code == 404:
                return {'status': 'success', 'exists': False, 'platform': platform, 'username': username}
            
            if self.platforms[platform]['error'].lower() in content.lower():
                return {'status': 'success', 'exists': False, 'platform': platform, 'username': username}
            else:
                return {'status': 'success', 'exists': True, 'platform': platform, 'username': username, 'url': url}
                
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def check_username_all_platforms(self, username):
        """Verifica un username su tutte le piattaforme supportate"""
        results = {}
        for platform in self.platforms:
            results[platform] = self.check_username(username, platform)
        return results

    def check_usernames_from_file(self, file_path):
        """Verifica una lista di username da un file di testo"""
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
        """Salva i risultati in un file di testo"""
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
                            exists = "Esiste" if data.get('exists') else "Non esiste"
                            file.write(f"{platform.capitalize()}: {exists}\n")
                            if data.get('url'):
                                file.write(f"  URL: {data['url']}\n")
            return {'status': 'success', 'message': f'Risultati salvati in {output_file}'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}