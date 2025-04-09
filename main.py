import requests
import hashlib

def check_password(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    for line in response.text.splitlines():
        if suffix in line:
            count = int(line.split(':')[1])
            print(f"⚠️ Password compromessa! Trovata in {count} violazioni.")
            return
    print("✅ Password sicura (non trovata in violazioni note).")

password = input("Inserisci la password da verificare: ")
check_password(password)