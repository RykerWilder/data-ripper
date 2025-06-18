from colorama import Fore, Style
import whois 
import requests

class GetDomainInfo:
    
    def get_domain_info(self, domain):
        try:
            domain_info = whois.whois(domain)
            return domain_info
        except Exception as e:
            return f"Errore durante il recupero delle informazioni WHOIS: {str(e)}"

    def domain_info_manager(self, domain):
        
        result = self.get_domain_info(domain)
        
        print(f"\n{Fore.GREEN}Informazioni WHOIS per {domain}:{Style.RESET_ALL}\n")
        print(result)