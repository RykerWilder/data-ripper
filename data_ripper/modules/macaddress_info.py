import requests
import json
import re
from colorama import Fore, Style

class MACLookup:
    def __init__(self, api_key=None):
        """
        Inizializza la classe MACLookup
        :param api_key: Chiave API opzionale per servizi che la richiedono
        """
        self.api_key = api_key
        self.base_url = "https://api.maclookup.app/v2/macs/"
        
    def validate_mac(self, mac_address):
        """
        Valida il formato del MAC address
        :param mac_address: MAC address da validare
        :return: True se valido, False altrimenti
        """
        # Rimuove eventuali separatori e converte in minuscolo
        clean_mac = re.sub(r'[:\-\.]', '', mac_address).lower()
        
        # Verifica la lunghezza (6 byte = 12 caratteri esadecimali)
        if len(clean_mac) != 12:
            return False
        
        # Verifica che siano tutti caratteri esadecimali validi
        if not re.match(r'^[0-9a-f]{12}$', clean_mac):
            return False
            
        return True
    
    def format_mac(self, mac_address):
        """
        Formatta il MAC address in un formato standard
        :param mac_address: MAC address da formattare
        :return: MAC address formattato
        """
        clean_mac = re.sub(r'[:\-\.]', '', mac_address).lower()
        return ':'.join(clean_mac[i:i+2] for i in range(0, 12, 2))
    
    def lookup(self, mac_address):
        """
        Esegue la ricerca del MAC address
        :param mac_address: MAC address da cercare
        :return: Dizionario con i risultati o None in caso di errore
        """
        if not self.validate_mac(mac_address):
            return {f"{Fore.RED}[X] Invalid MAC address format.{Style.RESET_ALL}"}
        
        formatted_mac = self.format_mac(mac_address)
        
        try:
            # Costruisce l'URL per la richiesta API
            url = f"{self.base_url}{formatted_mac}"
            
            # Effettua la richiesta HTTP
            response = requests.get(url, timeout=10)
            
            # Controlla lo status della risposta
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return {f"{Fore.RED}[X] API error: {response.status_code}{Style.RESET_ALL}"}
                
        except requests.exceptions.RequestException as e:
            return {f"{Fore.RED}[X] Connection error: {str(e)}{Style.RESET_ALL}"}
        except json.JSONDecodeError:
            return {f"{Fore.RED}[X] Parsing error.{Style.RESET_ALL}"}
    
    def get_vendor_info(self, mac_address):
        try:
            result = self.lookup(mac_address)  
            # Se result è un set (cioè contiene un messaggio di errore)
            if isinstance(result, set):
                # Estrae il messaggio di errore dal set
                error_message = next(iter(result)) if result else "Unknown error"
                print(f"{Fore.RED}{error_message}{Style.RESET_ALL}")
                return {"Vendor": "Unknown", "Address": "Unknown"}
        
            return {
                "Vendor": result.get('company'),
                "Address": result.get('address'),
                "Country": result.get('country'),
                "MAC Prefix": result.get('macPrefix'),
                "Block Type": result.get('blockType'),
                "Block Size": result.get('blockSize'),
                "Updated": result.get('updated'),
                "Is Random": result.get('isRand'),
                "Is Private": result.get('isPrivate')
            }
        
        except Exception as e:
            print(f"{Fore.RED}[X] Error during the info vendor recovery: {e}{Style.RESET_ALL}")
    
    def mac_address_manager(self, mac_input):          
        print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Loading...")
            
        # Esegue la ricerca
        result = self.get_vendor_info(mac_input)
            
        # Mostra i risultati
        if "error" in result:
            print(f"{Fore.RED}[X]  {result['error']}{Style.RESET_ALL}")
        else:
            for key, value in result.items():
                print(f"{key}: {value}")