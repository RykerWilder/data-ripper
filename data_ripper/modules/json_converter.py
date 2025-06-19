import json
from datetime import datetime

class JSONConverter:
    def __init__(self, json_data, output_filename=None):
        """
        Inizializza il converter con i dati JSON e un nome file opzionale
        
        :param json_data: Dati JSON da convertire (può essere stringa JSON o dict)
        :param output_filename: Nome del file di output (opzionale)
        """
        self.json_data = self._parse_json(json_data)
        self.output_filename = output_filename or self._generate_default_filename()
    
    def _parse_json(self, json_data):
        """Analizza i dati JSON indipendentemente dal formato di input"""
        if isinstance(json_data, str):
            try:
                return json.loads(json_data)
            except json.JSONDecodeError:
                raise ValueError("La stringa fornita non è un JSON valido")
        elif isinstance(json_data, dict):
            return json_data
        else:
            raise TypeError("Il tipo di dati fornito non è supportato (atteso: stringa JSON o dict)")
    
    def _generate_default_filename(self):
        """Genera un nome file di default basato sulla data/ora"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"domain_results_{timestamp}.txt"
    
    def _format_value(self, value, indent_level=0):
        """Formatta i valori in modo leggibile"""
        indent = "  " * indent_level
        
        if isinstance(value, dict):
            return self._format_dict(value, indent_level)
        elif isinstance(value, list):
            return self._format_list(value, indent_level)
        elif isinstance(value, str):
            return f'"{value}"'
        else:
            return str(value)
    
    def _format_dict(self, data_dict, indent_level):
        """Formatta un dizionario in modo leggibile"""
        lines = []
        indent = "  " * indent_level
        
        for key, value in data_dict.items():
            formatted_value = self._format_value(value, indent_level + 1)
            lines.append(f"{indent}{key}: {formatted_value}")
        
        return "\n".join(lines)
    
    def _format_list(self, data_list, indent_level):
        """Formatta una lista in modo leggibile"""
        lines = []
        indent = "  " * indent_level
        
        for i, item in enumerate(data_list):
            formatted_item = self._format_value(item, indent_level + 1)
            lines.append(f"{indent}[{i}]: {formatted_item}")
        
        return "\n".join(lines)
    
    def convert_to_txt(self, custom_filename=None):
        """
        Converte i dati JSON in un file TXT
        
        :param custom_filename: Nome file personalizzato (opzionale)
        :return: Il percorso del file generato
        """
        output_file = custom_filename or self.output_filename
        
        try:
            formatted_output = self._format_value(self.json_data)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("=== Risultati Information Gathering ===\n")
                f.write(f"Generato il: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(formatted_output)
            
            return output_file
        except Exception as e:
            raise IOError(f"Errore durante la scrittura del file: {str(e)}")
