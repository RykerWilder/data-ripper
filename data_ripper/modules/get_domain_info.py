from data_ripper.modules.json_converter import JSONConverter
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
        
        converter = JSONConverter(result)
        output_path = converter.convert_to_txt()
        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} File generated successfully: {Fore.BLUE}{output_path}{Style.RESET_ALL}")