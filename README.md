# dad-bea
Auto login The Bank of East Asia (HKBEA) Cyberbanking account.

# Requirements
- Linux / MacOS
    - Chromium OR Chrome + chromedriver
    - curl
- Python 3.5+
    - selenium

# Usage
`$ ACCT_NO=00011122233344 ACCT_PIN=abcd1234 python3 main.py`

# Action
![Action](https://drop.wtako.net/file/231d02743612e9303c8a1dbdf0bf3e362cc57404.gif)

# Why
HKBEA's dynamic password feature is stupid, requires linear search for human brains, not proven to actually improve security, can only be used by mouse. It is extremely annoying to login if there is no automation.
