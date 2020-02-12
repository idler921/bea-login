# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 17:05:37 2019

https://github.com/Saren-Arterius/dad-bea/blob/master/main.py

@author: Saren Arterius

@author: idler@gmail.com update for 2020 login

"""

#from subprocess import check_output
from selenium import webdriver
#from time import sleep
#from os import environ
import requests
import hashlib
import base64
import os
import time

def get_digit_map_2019(browser):
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
        #print(path)
        path2 = f"https://mobile.hkbea-cyberbanking.com{path}"
        #print(path2)
        r = s.get(path2)
        #sha256 = check_output(
            #f'curl -s \'https://mobile.hkbea-cyberbanking.com{path}\' -H \'Cookie: {cookies_arg}\' --compressed | sha256sum | awk \'{{print $1}}\'', shell=True).decode().strip()
        sha256 = hashlib.sha256(r.content).hexdigest()
        #print(i, path2, sha256, sha256_map[sha256])
        digit_map[sha256_map[sha256]] = str(i)
    print(digit_map)
    return digit_map


def get_digit_map_2020():
    sha256sum_output = """
    d39281ec5c5d674a30244bab11cb78dce3330d760a897f184cd849319fe21942 0
    2dc0f821c6653f14180826500f5386cf8c83e301ffe32ce4e7d35f3c662c16d7 1
    5e81bb3f7cdf807b8c8051c604f31d5041630ed7944fb79afa18c5a1c1b25805 2
    f2f2193482d738448a8d3c4aec7747b26ad4fe144d652ed3b731995e396c8232 3
    46c5b720e56643b0e2b952ff21e4e56872e9d6ee69bba1296011ae48cd4fd838 4
    e478531532757ca08e8904cf0f1966917910e7ea300ffcf44dee38fe1ae6f0b8 5
    cf2a9b092879ccbe985d26cc405e4849385cece6638a1792fd7bf979baab8621 6
    c607e404663427c4550816676c9a1a160c964e927f6e7ecc0d1a9d6e04d2bc77 7
    169c9dcbfe4ca16a8be81737ead6d11f22284efdd035179a7a344f86db917560 8
    a1c6c48ad97b056cee9b085cecfcd57371218d2753210088d1f41f336732d4d0 9
    """

    sha256_map = {}
    tmp = sha256sum_output.split()
    for i in range(int(len(tmp) / 2)):
        sha256_map[tmp[i * 2]] = tmp[i * 2 + 1]

    digit_map = {}
    for i in range(10):
        path = b.find_element_by_xpath("//div[@key-value='" + str(i) + "']/img").get_attribute("src")
        r = s.get(path)
        sha256 = hashlib.sha256(r.content).hexdigest()
        print(i, path, sha256, sha256_map[sha256])
        digit_map[sha256_map[sha256]] = str(i)
    print(digit_map)
    return digit_map

def print_sha_map():
    for i in range(10):
        path = b.find_element_by_xpath("//div[@key-value='" + str(i) + "']/img").get_attribute("src")
        r = s.get(path)
        sha256 = hashlib.sha256(r.content).hexdigest()
        print(str(i) + " " + sha256)


def main():

    ac_no = environ['ACCT_NO']
    ac_pw = environ['ACCT_PIN']

    driver_path = "c:/lib/chromedriver.exe" # use your path, for windows

    if os.path.isfile(driver_path):
        b = webdriver.Chrome(driver_path)
    else:
        b = webdriver.Chrome()


    b.implicitly_wait(5)


    #b.get('https://mobile.hkbea-cyberbanking.com/servlet/FRLogon?Lang=Big5&isFromPB=N')
    #b.get('https://mobile.hkbea-cyberbanking.com/servlet/FRLogon?isFromPB=N')
    b.get('https://www.hkbea-cyberbanking.com/ibk/auth/web/login?Lang=Eng&beacookieid=')

    b.find_element_by_css_selector('#AcctNo').send_keys(ac_no)
    b.find_element_by_css_selector('#actPwdLabel').click()

    s = requests.Session()
    for cookie in b.get_cookies():
        s.cookies.set(cookie['name'], cookie['value'])

    digit_map = get_digit_map_2020()    

    for c in ac_pw:
        if c.isdigit():
            #b.find_element_by_css_selector(f'.key{digit_map[c]}').click()
            b.find_element_by_xpath("//div[@key-value='" + str(digit_map[c]) + "']").click()
        else:
            #b.find_element_by_css_selector(f'.key{c.upper()}').click()
            b.find_element_by_xpath("//img[@src='/web/resource/logon2/fullkeypad/" + c.upper() + ".png']").click()

    b.find_element_by_css_selector('#loginBtn').click()

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
