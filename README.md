# Klock

**Klock** is a powerful  Python-based PDF password cracking tool that supports both wordlist and brute-force attacks. It is designed to help recover lost or forgotten passwords for PDF files.

---

## Features

- Brute-force attack using key combinations.
- Wordlist-based attack to attempt password recovery.
- Multithreaded for faster cracking.
- Minimalistic and interactive command-line interface.

---

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/bayazid-bit/klock.git
Install the required dependencies:

```bash

   pip install PyMuPDF
Run the tool:

```bash

python klock.py
Usage
Wordlist Attack

Use a predefined wordlist to try potential passwords.
Example:


python klock.py
When prompted, choose the wordlist method and provide the path to your wordlist.
Brute-force Attack

You can specify the key combination (e.g., lowercase, digits) and the length range of the password.
Example:
bash

python klock.py
When prompted, choose the key combination method and enter the required parameters like key characters, min and max password lengths.
Example
bash

python klock.py

[*] Enter PDF file path: secret.pdf
[1] Crack by word list
[2] Crack by key combination
> 1
[*] Enter word list path: /path/to/wordlist.txt
[~] Running brute-force attack...



python klock.py

[*] Enter PDF file path: secret.pdf
[1] Crack by word list
[2] Crack by key combination
> 2
[*] Enter key combination (e.g., abc123 for lowercase letters and digits): abc123
[*] Enter min length of password: 4
[*] Enter max length of password: 6
[*] Show current key (it will make the process slower)<yes>/<no>: no
[~] Running brute-force attack...


License
This project is licensed under the MIT License. See the LICENSE file for more details.

Disclaimer
Klock is for educational purposes only. Unauthorized access to PDF files or any password-protected material without permission is illegal. The developer is not responsible for any misuse of this tool.

Contact
Author: MD. Bayazid
Email: bayazid.mtu@gmail.com
