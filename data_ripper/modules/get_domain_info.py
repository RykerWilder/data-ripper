from colorama import Fore, Style
import whois 
import requests

class GetDomainInfo:
    
    def get_domain_info(self, domain):
        try:
            domain_info = whois.whois(domain)
            return domain_info
        except Exception as e:
            return f"{Fore.RED}[X] Error retrieving WHOIS information: {str(e)}{Style.RESET_ALL}"

    def domain_info_manager(self, domain):
        
        result = self.get_domain_info(domain)
        
        # print(f"\n{Fore.BLUE}[INFO]{Style.RESET_ALL} WHOIS information for {Fore.BLUE}{domain}{Style.RESET_ALL}:\n")
        # print(result)
        
        converter = JSONToTXTConverter(result)
        output_path = converter.convert_to_txt()
        print(f"File generato con successo: {output_path}")