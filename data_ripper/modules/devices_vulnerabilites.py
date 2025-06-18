from dotenv import load_dotenv
import os
import shodan

class DevicesVulnerabilities():

    api_key = os.getenv("SHODAN_API_KEY")
    api = shodan.Shodan(api_key)

    def search_shodan(query):
    try:
        results = api.search(query)
        for result in results['matches']:
            print(f"IP: {result['ip_str']}")
            print(f"Port: {result['port']}")
            print(f"Data: {result['data'][:100]}...\n")
    except shodan.APIError as e:
        print(f"Error: {e}")