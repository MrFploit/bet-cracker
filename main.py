import os, time

os.system("clear")
b1 = '''
\033[91m
  _______    _        _             
 |__   __|  | |      | |            
    | | __ _| |_ __ _| | ___   ___  
    | |/ _` | __/ _` | |/ _ \ / _ \ 
    | | (_| | || (_| | | (_) | (_) |
    |_|\__,_|\__\__,_|_|\___/ \___/ 
    
'''
b2 = '''
\033[92m
  _  __                           _     
 | |/ /                          | |    
 | ' / ___  _ __ _____      _____| |__  
 |  < / _ \| '__/ _ \ \ /\ / / __| '_ \ 
 | . \ (_) | | | (_) \ V  V /\__ \ | | |
 |_|\_\___/|_|  \___/ \_/\_/ |___/_| |_|
                                        
'''
b3 = '''
\033[93m
  _                       _            
 (_)                     | |           
  _ _ __   __ _ _   _  __| | __ _ _ __ 
 | | '_ \ / _` | | | |/ _` |/ _` | '__|
 | | |_) | (_| | |_| | (_| | (_| | |   
 |_| .__/ \__,_|\__, |\__,_|\__,_|_|   
   | |           __/ |                 
   |_|          |___/               
   
'''
b4 = '''
\033[94m
 __          __   _  __ ____       _   
 \ \        / /  | |/ _|  _ \     | |  
  \ \  /\  / /__ | | |_| |_) | ___| |_ 
   \ \/  \/ / _ \| |  _|  _ < / _ \ __|
    \  /\  / (_) | | | | |_) |  __/ |_ 
     \/  \/ \___/|_|_| |____/ \___|\__|
                                       
'''
b5 = '''
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

b6 = '''
\033[96m
  _____            ____                    
 |  __ \          |  _ \                   
 | |__) |__   ___ | |_) | ___   ___  _ __  
 |  ___/ _ \ / _ \|  _ < / _ \ / _ \| '_ \ 
 | |  | (_) | (_) | |_) | (_) | (_) | | | |
 |_|   \___/ \___/|____/ \___/ \___/|_| |_|
                                           
'''

b7 = '''
\033[93m                _                   
     /\        (_)                  
    /  \   _ __ _  __ _ _ __   __ _ 
   / /\ \ | '__| |/ _` | '_ \ / _` |
  / ____ \| |  | | (_| | | | | (_| |
 /_/    \_\_|  |_|\__,_|_| |_|\__,_|
                      
'''

b8 = '''
\033[92m
  _      _ _        
 | |    (_) |       
 | | ___ _| |_ ___  
 | |/ _ \ | __/ _ \ 
 | |  __/ | || (_) |
 |_|\___|_|\__\___/ 
                    
'''

b9 = '''
\033[94m
                _           
               | |          
  ___  __ _ ___| |__   __ _ 
 / __|/ _` / __| '_ \ / _` |
 \__ \ (_| \__ \ | | | (_| |
 |___/\__,_|___/_| |_|\__,_|

'''

print(b1)
time.sleep(0.3)
os.system("clear")
print(b2)
time.sleep(0.3)
os.system("clear")
print(b3)
time.sleep(0.3)
os.system("clear")
print(b4)
time.sleep(0.3)
os.system("clear")
print(b5)
time.sleep(0.3)
os.system("clear")
print(b6)
time.sleep(0.3)
os.system("clear")
print(b7)
time.sleep(0.3)
os.system("clear")
print(b8)
time.sleep(0.3)
os.system("clear")
print(b9)
time.sleep(0.3)
os.system("clear")

def choise():
    print ('''
    \033[92m  ____       _                          
    \033[92m |  _ \     | |                         
    \033[92m | |_) | ___| |_                        
    \033[92m |  _ < / _ \ __|                       
    \033[92m | |_) |  __/ |_                        
    \033[92m |____/_\___|\__|  
    \033[95m       _             
    \033[95m    / ____|              | |            
    \033[95m   | |     _ __ __ _  ___| | _____ _ __ 
    \033[95m   | |    | '__/ _` |/ __| |/ / _ \ '__|
    \033[95m   | |____| | | (_| | (__|   <  __/ |   
    \033[95m    \_____|_|  \__,_|\___|_|\_\___|_|   
\033[92m           
      Code by it4min
      t.me/LinuxArmy
      https://github.com/it4min/betcracker     
\033[95m           
    [1] Tataloo          [6] sasha sobhani
    [2] Wolf Bet         [7] leito
    [3] ipaydar          [8] poo boon           
    [4] donya            [9] ariana
    [5] kooroowsh        
                                        
    ''')
    numbet = input("\033[93m[\033[91m*\033[93m]\033[96m Please enter the site number>>> ")

    if numbet == '1':
	    os.system("python tatal.py")
    elif numbet == '2':
	    os.system("python wolfbet.py")
    elif numbet == '3':
	    os.system("python 8loco.py")
    elif numbet == '4':
	    os.system("python donya.py")
    elif numbet == '5':
	    os.system("python korosh.py")
    elif numbet == '6':
	    os.system("python sasha.py")
    elif numbet == '7':
	    os.system("python leito.py")
    elif numbet == '8':
	    os.system("python pooboon.py")
    elif numbet == '9':
	    os.system("python ariana.py")
    else:
	    print("\033[93mwarning: Please select the correct number!")
	    time.sleep(4)
	    os.system("clear")
	    choise()
choise()

