import string, json, requests, random
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep

system('cls')
boucle1 = True
boucle2 = True
failed_previous = False

sent_count = 0

def random_number(digits):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return random.randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def send_message(webhook_url):
    username = id_generator(80)
    message = """ 
    ```
    ไอ ลูก หมา
  3P3KLIGI18KUCVPKIXJIVKINP3RY3Y8AAFMTTIQFFBJXRGEMED1SF93O6QQ2WSZXCQPHP552CRF72P04
  ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ
ՎԾՄ Գɿעȝ ʍȝ Եɧȝ ƙɿՌԺ ԾԲ ԲȝȝʅɿՌԳ ρȝԾρʅȝ աՐɿԵȝ ՌԾעȝʅՏ ԹՅԾՄԵ.
ՎԾՄ Գɿעȝ ʍȝ Եɧȝ ƙɿՌԺ ԾԲ ԲȝȝʅɿՌԳ ρȝԾρʅȝ աՐɿԵȝ ՌԾעȝʅՏ ԹՅԾՄԵ.
ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ
ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ
ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ




ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ





ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ





ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ





ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ




ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ
 ```
 https://cdn.discordapp.com/attachments/1009902723732357202/1010966357967372420/f458cc675c965207d4a0ee81d78252bc.gif
@everyone  https://discord.gg/4daHfJ9PR2

    
  
"""
    avatar = "https://cdn.discordapp.com/attachments/1009902723732357202/1010192764358643862/images.jpeg"
    data = json.dumps({
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": False
    })

    header = {
        "content-type": "application/json"
    }

    response = requests.post(webhook_url, data, headers=header)
    print(Colorate.Horizontal(Colors.rainbow, f"{username}"))

header_final = """

   )  (  .  (   (  (   (( (         ( .  (   ((    ((      
  ()) )\  . )\  )\ )\ (\())\        )\ . )\  ))\  (\()     
 (()))(_)  ((_)((_)(_))(_)(_)      ((_) ((_)((_))))(_)     
(/ __| _ \/ _ \\ \ / / __| _ \    |_  // _ \| \| | __|     
| (_ |   / (_) |\   /| _||   /     / /| (_) | .  | _|      
 \___|_|_\\___/  \_/ |___|_|_\    /___|\___/|_|\_|___|     

                                                             
 - """

while boucle1:
    print(Colorate.Horizontal(Colors.rainbow,  Center.XCenter(header_final)))
    webhook_url = input("[?]   WEBHOOK URL:  ")
    if webhook_url.startswith(f"{webhook_url}"):
        boucle1 = False
        system('cls')
    else:
        system('cls')
        print(Colorate.Horizontal(Colors.black_to_red, Center.XCenter(header_final)))
        print(Colorate.Horizontal(Colors.black_to_red, "[!] Please insert a valid link !"))
        sleep(2)
        system('cls')

while boucle2:
    if (send_message(webhook_url)):
        sent_import string, json, requests, random
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep

system('cls')
boucle1 = True
boucle2 = True
failed_previous = False

sent_count = 0

def random_number(digits):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return random.randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def send_message(webhook_url):
    username = id_generator(80)
    message = """ 
    ```
    ไอ ลูก หมา
  3P3KLIGI18KUCVPKIXJIVKINP3RY3Y8AAFMTTIQFFBJXRGEMED1SF93O6QQ2WSZXCQPHP552CRF72P04
  ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ
ՎԾՄ Գɿעȝ ʍȝ Եɧȝ ƙɿՌԺ ԾԲ ԲȝȝʅɿՌԳ ρȝԾρʅȝ աՐɿԵȝ ՌԾעȝʅՏ ԹՅԾՄԵ.
ՎԾՄ Գɿעȝ ʍȝ Եɧȝ ƙɿՌԺ ԾԲ ԲȝȝʅɿՌԳ ρȝԾρʅȝ աՐɿԵȝ ՌԾעȝʅՏ ԹՅԾՄԵ.
ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ
ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ
ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ




ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ





ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ





ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ





ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ




ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ
 ```
 https://cdn.discordapp.com/attachments/1009902723732357202/1010966357967372420/f458cc675c965207d4a0ee81d78252bc.gif
@everyone  https://discord.gg/4daHfJ9PR2

    
  
"""
    avatar = "https://cdn.discordapp.com/attachments/1009902723732357202/1010192764358643862/images.jpeg"
    data = json.dumps({
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": False
    })

    header = {
        "content-type": "application/json"
    }

    response = requests.post(webhook_url, data, headers=header)
    print(Colorate.Horizontal(Colors.rainbow, f"{username}"))

header_final = """

   )  (  .  (   (  (   (( (         ( .  (   ((    ((      
  ()) )\  . )\  )\ )\ (\())\        )\ . )\  ))\  (\()     
 (()))(_)  ((_)((_)(_))(_)(_)      ((_) ((_)((_))))(_)     
(/ __| _ \/ _ \\ \ / / __| _ \    |_  // _ \| \| | __|     
| (_ |   / (_) |\   /| _||   /     / /| (_) | .  | _|      
 \___|_|_\\___/  \_/ |___|_|_\    /___|\___/|_|\_|___|     

                                                             
 - """

while boucle1:
    print(Colorate.Horizontal(Colors.rainbow,  Center.XCenter(header_final)))
    webhook_url = input("[?]   WEBHOOK URL:  ")
    if webhook_url.startswith(f"{webhook_url}"):
        boucle1 = False
        system('cls')
    else:
        system('cls')
        print(Colorate.Horizontal(Colors.black_to_red, Center.XCenter(header_final)))
        print(Colorate.Horizontal(Colors.black_to_red, "[!] Please insert a valid link !"))
        sleep(2)
        system('cls')

while boucle2:
    if (send_message(webhook_url)):
        sent_import string, json, requests, random
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep

system('cls')
boucle1 = True
boucle2 = True
failed_previous = False

sent_count = 0

def random_number(digits):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return random.randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def send_message(webhook_url):
    username = id_generator(80)
    message = """ 
    ```
    ไอ ลูก หมา
  3P3KLIGI18KUCVPKIXJIVKINP3RY3Y8AAFMTTIQFFBJXRGEMED1SF93O6QQ2WSZXCQPHP552CRF72P04
  ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ
ՎԾՄ Գɿעȝ ʍȝ Եɧȝ ƙɿՌԺ ԾԲ ԲȝȝʅɿՌԳ ρȝԾρʅȝ աՐɿԵȝ ՌԾעȝʅՏ ԹՅԾՄԵ.
ՎԾՄ Գɿעȝ ʍȝ Եɧȝ ƙɿՌԺ ԾԲ ԲȝȝʅɿՌԳ ρȝԾρʅȝ աՐɿԵȝ ՌԾעȝʅՏ ԹՅԾՄԵ.
ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ
ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ
ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ




ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ





ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ





ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ





ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ




ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒｲ 乇dﾉｲo尺ｲ乇ﾒ
 ```
 https://cdn.discordapp.com/attachments/1009902723732357202/1010966357967372420/f458cc675c965207d4a0ee81d78252bc.gif
@everyone  https://discord.gg/SAQ9G5H95v

    
  
"""
    avatar = "https://cdn.discordapp.com/attachments/1009902723732357202/1010192764358643862/images.jpeg"
    data = json.dumps({
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": False
    })

    header = {
        "content-type": "application/json"
    }

    response = requests.post(webhook_url, data, headers=header)
    print(Colorate.Horizontal(Colors.rainbow, f"{username}"))

header_final = """

   )  (  .  (   (  (   (( (         ( .  (   ((    ((      
  ()) )\  . )\  )\ )\ (\())\        )\ . )\  ))\  (\()     
 (()))(_)  ((_)((_)(_))(_)(_)      ((_) ((_)((_))))(_)     
(/ __| _ \/ _ \\ \ / / __| _ \    |_  // _ \| \| | __|     
| (_ |   / (_) |\   /| _||   /     / /| (_) | .  | _|      
 \___|_|_\\___/  \_/ |___|_|_\    /___|\___/|_|\_|___|     

                                                             
 - """

while boucle1:
    print(Colorate.Horizontal(Colors.rainbow,  Center.XCenter(header_final)))
    webhook_url = input("[?]   WEBHOOK URL:  ")
    if webhook_url.startswith(f"{webhook_url}"):
        boucle1 = False
        system('cls')
    else:
        system('cls')
        print(Colorate.Horizontal(Colors.black_to_red, Center.XCenter(header_final)))
        print(Colorate.Horizontal(Colors.black_to_red, "[!] Please insert a valid link !"))
        sleep(2)
        system('cls')

while boucle2:
    if (send_message(webhook_url)):
        sent_count += 1
