import requests
import json
import re

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
            return {"error": "Formato MAC address non valido"}
        
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
                return {"error": f"Errore API: {response.status_code}"}
                
        except requests.exceptions.RequestException as e:
            return {"error": f"Errore di connessione: {str(e)}"}
        except json.JSONDecodeError:
            return {"error": "Errore nel parsing della risposta JSON"}
    
    def get_vendor_info(self, mac_address):
        """
        Ottiene informazioni specifiche sul vendor
        :param mac_address: MAC address da cercare
        :return: Informazioni sul vendor o messaggio di errore
        """
        result = self.lookup(mac_address)
        
        if "error" in result:
            return result
        
        vendor_info = {
            "MAC Address": self.format_mac(mac_address),
            "Vendor": result.get('company', 'Sconosciuto'),
            "Address": result.get('address', 'Non disponibile'),
            "Country": result.get('country', 'Non disponibile'),
            "Type": result.get('type', 'Non disponibile'),
            "Is Private": result.get('isPrivate', 'Non disponibile')
        }
        
        return vendor_info
    
    def interactive_lookup(self):
        """
        Modalità interattiva per l'input utente
        """
        print("=== MAC Address Lookup Tool ===")
        print("Inserisci 'quit' per uscire")
        print("-" * 40)
        
        while True:
            mac_input = input("\nInserisci il MAC address: ").strip()
            
            if mac_input.lower() in ['quit', 'exit', 'q']:
                print("Arrivederci!")
                break
            
            if not mac_input:
                print("Per favore, inserisci un MAC address.")
                continue
            
            print("\nRicerca in corso...")
            
            # Esegue la ricerca
            result = self.get_vendor_info(mac_input)
            
            # Mostra i risultati
            if "error" in result:
                print(f"❌ Errore: {result['error']}")
            else:
                print("✅ Risultati della ricerca:")
                print("-" * 30)
                for key, value in result.items():
                    print(f"{key}: {value}")
                print("-" * 30)

# Esempio di utilizzo
if __name__ == "__main__":
    # Crea un'istanza della classe
    mac_lookup = MACLookup()
    
    # Modalità interattiva
    mac_lookup.interactive_lookup()
    
    # Oppure uso programmatico
    # result = mac_lookup.get_vendor_info("00:1A:2B:3C:4D:5E")
    # print(result)