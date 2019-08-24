#!/usr/bin/env python3
from subprocess import check_output
from selenium import webdriver
from time import sleep
from os import environ
import requests
import hashlib


def get_digit_map(browser):
    sha256sum_output = """
    01c32384a0494deb34702fce7556770adbbd1e61357356fc8e9031bf1ad76a81  0.gif
    9764486b699d7355cea0c5288bf3fe36ed64cd7c8e61cd95f2428c9a005b4be5  1.gif
    91dcf14def3c813da9eb51ed18bdbaae443a296f0d6507ed1c192b9ff6c1e5fb  2.gif
    6ad905cb0a69cfd423cadf7a0542be6e3454fd7d0fb0d21c7b5a5be0206fe5ac  3.gif
    232d196b73df4d9a98e9ed3c8a4e4267b9850796faa5c99b187aa537cf33fb1b  4.gif
    6589c4a948fa3e0a9b15c11f40b580ce42f05c2cd48ac9a1dad89a331b76626b  5.gif
    faa85a378e523bd558cf03ee33a99bbc96d12749e63ba9d622f4b3ab65f4b590  6.gif
    58251cf8e119f13ed542f114e7af7a6d41898f1eeb956131f432bff9ae9eefd8  7.gif
    5cb38d5c573eab00e8442366b7fc7a0c6fe119b63add7eaef1c0a4b1066c0a7d  8.gif
    99e25bc2eaa143f1d8650fba4ab1db7e1cf730b4bdededfdee65e35ec51db6df  9.gif
    """

    sha256_map = {}
    tmp = sha256sum_output.split()
    for i in range(int(len(tmp) / 2)):
        sha256_map[tmp[i * 2]] = tmp[i * 2 + 1].split('.')[0]

    #cookies_arg = '; '.join(map(lambda c: f"{c['name']}={c['value']}", browser.get_cookies()))
    s = requests.Session()
    for cookie in browser.get_cookies():
        s.cookies.set(cookie['name'], cookie['value'])

    digit_map = {}
    for i in range(10):
        path = browser.find_element_by_css_selector(f'.key{i}').get_attribute('style').split('"')[1]
        path2 = f"https://mobile.hkbea-cyberbanking.com{path}"
        r = s.get(path2)
        sha256 = hashlib.sha256(r.content).hexdigest()
        print(i, path2, sha256, sha256_map[sha256])
        digit_map[sha256_map[sha256]] = str(i)
    print(digit_map)
    return digit_map


def main():
    b = webdriver.Chrome()
    b.get('https://mobile.hkbea-cyberbanking.com/servlet/FRLogon?Lang=Big5&isFromPB=N')

    b.find_element_by_css_selector('#CybAcctNo').send_keys(environ['ACCT_NO'])
    digit_map = get_digit_map(b)
    for c in environ['ACCT_PIN']:
        if c.isdigit():
            b.find_element_by_css_selector(f'.key{digit_map[c]}').click()
        else:
            b.find_element_by_css_selector(f'.key{c.upper()}').click()

    b.find_element_by_css_selector('#btnlogin').click()

    # HKBEA would prompt you to change your password, let's ignore it if needed
    try:
        b.find_element_by_css_selector(
            'body > div.wrapper > form > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(2) > a').click()  # forced click continue
        b.find_element_by_css_selector(
            'body > div.wrapper > form > table > tbody > tr:nth-child(5) > td > table > tbody > tr > td > a:nth-child(3)').click()  # cancel change password
        b.find_element_by_css_selector('#act_next').click()  # enable otp later
    except:
        pass

    print('You can now use the browser. Ctrl + C to exit.')
    while True:
        sleep(1000)


if __name__ == '__main__':
    main()
