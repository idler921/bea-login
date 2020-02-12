# bea-login
Auto login The Bank of East Asia (HKBEA) Cyberbanking account.

# Requirements
- Linux / MacOS / Windows
    - Chromium OR Chrome + chromedriver

- Python 3.5+
    - selenium

# Usage
`$ ACCT_NO=00011122233344 ACCT_PIN=abcd1234 python3 main.py`

# Why
HKBEA's dynamic password feature is stupid, requires linear search for human brains, not proven to actually improve security, can only be used by mouse. It is extremely annoying to login if there is no automation.
