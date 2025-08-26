# Data Ripper

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![data_ripper](./data-ripper/assets/data-ripper.png)

Data Ripper is an **Information Gathering Tool**, which allows you to:
1. Check if your password has been found in data breaches via HaveIBeenPwneed.
2. Check if your email has been found in data breaches via HaveIBeenPwneed.
3. Receive information about a domain that will be saved in a file called "domain_results_{current_date}.txt"
4. Find out if a username or a username list exist on Github, Pinterest, Facebook, Twitter, Instagram, Reddit. In the event that you have a username list, you can insert a file called "username.txt" in the root of the project and the software will return a "username_results.txt" file with the results.

---

### Prerequisites
- Python 3.x

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```