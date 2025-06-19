from colorama import Fore, Style
import sys

def exit(signum, frame):
    print(f"\n{Fore.RED}[X] Data Ripper stopped{Style.RESET_ALL}")
    sys.exit(0)

def print_welcome_message():
      print(f"""{Fore.RED}
      ___________________   ___________________
  .-/|  78   ~~**~~      \ /      ~~**~~   79  |\-.
  ||||                    :                    ||||
  ||||      Welcome       :        Coded       ||||
  ||||                    :                    ||||
  ||||         To         :          By        ||||
  ||||                    :                    ||||
  ||||        Data        :      RykerWilder   ||||
  ||||                    :                    ||||
  ||||       Ripper       :                    ||||
  ||||                    :                    ||||
  ||||                    :                    ||||
  ||||                    :                    ||||
  ||||___________________ : ___________________||||
  ||/====================\:/====================\||
  `---------------------~___~--------------------''

  {Fore.YELLOW}Press CTRL+C to quit.
{Style.RESET_ALL}""")
