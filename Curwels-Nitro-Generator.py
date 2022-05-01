import os
import random
import string
import time
import ctypes

try: 
    from discord_webhook import DiscordWebhook 
except ImportError: 
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") 
    exit() 
try: 
    import requests 
except ImportError: 
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit() 


class NitroGen:
    def __init__(self): 
        self.fileName = "Nitro Codes.txt" 

    def main(self): 
        os.system('cls' if os.name == 'nt' else 'clear') 
        if os.name == "nt": 
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Thendra")
        else: 
            print(f'\33]0;Nitro Generator and Checker - Curwels\a', end='', flush=True) 

        time.sleep(1) 
        self.slowType("Nitro Generator Programına Hoş Geldiniz!", .02) 
        time.sleep(1) 
        self.slowType("\nKaç Kod Üretileceğini ve Kontrol Edileceğini Giriniz: ", .02, newLine = False) 

        num = int(input('')) 

    
        self.slowType("\nBir Discord Webhook Adresi Girin! \nEğer Istiyorsanız Buraya Yazın veya Yoksaymak için Enter Tuşuna Basın: ", .02, newLine = False)
        url = input('') 
        webhook = url if url != "" else None 

   

        valid = [] 
        invalid = 0 

        for i in range(num): 
            try: 
                code = "".join(random.choices( 
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}" 

                result = self.quickChecker(url, webhook) 

                if result: 
                    valid.append(url) 
                else: 
                    invalid += 1 
            except Exception as e: 
                print(f" Error | {url} ") 

            if os.name == "nt": 
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Üretici - {len(valid)} Geçerli | {invalid} Geçersiz -") 
                print("")
            else: 
                print(f'\33]0;Nitro Üretici - {len(valid)} Geçerli | {invalid} Geçersiz - \a', end='', flush=True) 

        print(f"""
Sonuçlar:
 Geçerli: {len(valid)}
 Geçersiz: {invalid}
 Geçerli Kodlar: {', '.join(valid )}""") 

        input("\nProgramı kapatmak için Enter tuşuna basın.") 
        [input(i) for i in range(1,0,-1)] 


    def slowType(self, text, speed, newLine = True): 
        for i in text: 
            print(i, end = "", flush = True) 
            time.sleep(speed) 
        if newLine: 
            print() 

    def generator(self, amount): 
        with open(self.fileName, "w", encoding="utf-8") as file: 
            print("Bekle, Nitro kodları üretiliyor.") 

            start = time.time() 

            for i in range(amount): 
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) 

                file.write(f"https://discord.gift/{code}\n") 

            
            print(f"{amount} Kod Üretildi | Geçen zaman: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None): 
        valid = []
        invalid = 0 
        with open(self.fileName, "r", encoding="utf-8") as file: 
            for line in file.readlines(): 
                nitro = line.strip("\n") 

               
                url = f"https://discord.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) 

                if response.status_code == 200: 
                    print(f" Geçerli | {nitro} ") 
                    valid.append(nitro) 

                    if notify is not None: 
                        DiscordWebhook( 
                            url = notify,
                            content = f"Geçerli Nitro Kodu algılandı! @everyone \n{nitro}"
                        ).execute()
                    else: 
                        break 

                else: 
                    print(f" Geçersiz | {nitro} ") 
                    invalid += 1 

        return {"valid" : valid, "invalid" : invalid} 

    def quickChecker(self, nitro, notify = None): 
        # Generate the request url
        url = f"https://discord.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) 

        if response.status_code == 200: 
            print(f" Geçerli | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") 
            with open("Nitro Codes.txt", "w") as file: 
                file.write(nitro) 

            if notify is not None: 
                DiscordWebhook( 
                    url = notify,
                    content = f"Geçerli Nito Algılandı! @everyone \n{nitro}"
                ).execute()

            return True 

        else: 
            print(f" Geçersiz | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") 
            return False 

if __name__ == '__main__':
    Gen = NitroGen() 
    Gen.main() 
