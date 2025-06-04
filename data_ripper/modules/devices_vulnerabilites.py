from dotenv import load_dotenv
import os
import shodan

class DevicesVulnerabilities():

    api_key = os.getenv("SHODAN_API_KEY")

    api = shodan.Shodan(api_key)