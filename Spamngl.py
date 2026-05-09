#!/usr/bin/env python3
#DIBAGUNOAN OLEH MAN FORCE X / CYBER FORCE X
#KELANTAN IT GUA MUSANG 18300 MALAYSIA KESEDAR KELANTAN DAERAH BANDAR GUA MUSANG MALAYSIA KOTA BHARU MALAYSIA PASIR MAS KELANTAN TANAH MERAH KELANTAN KUALA KRAI KELANTAN BACHOK KELANTAN GUA MUSANG KELANTAN 

"""
NGL SPAMMER - PRECISION EDITION
EXACT HITS • CHAT SUPPORT • SOUND EFFECTS
"""
import requests
import time
import sys
import threading
import random
import os
import webbrowser
import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# ==================== SOUND SYSTEM ====================
class SoundSystem:
    @staticmethod
    def play_sound():
        sound_url = "https://files.catbox.moe/vwqpdm.m4a"
        print(f"\033[96mSound URL: {sound_url}\033[0m")
        
        try:
            system = platform.system()
            if system == "Darwin":
                subprocess.run(['afplay', sound_url], timeout=5)
            elif system == "Linux":
                subprocess.run(['mpg123', sound_url], timeout=5)
            elif system == "Windows":
                os.startfile(sound_url)
        except:
            pass

# ==================== ANIMATION SYSTEM ====================
class Animations:
    @staticmethod
    def loading(text, duration=2):
        frames = ["|", "/", "-", "\\"]
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            sys.stdout.write(f"\r\033[96m{frames[i % len(frames)]} {text}\033[0m")
            sys.stdout.flush()
            time.sleep(0.2)
            i += 1
        print()
    
    @staticmethod
    def precision_load(count):
        print(f"\033[92mPrecision Mode: Targeting {count} exact hits\033[0m")
        for i in range(3):
            sys.stdout.write(f"\r\033[93mCalibrating target...\033[0m")
            sys.stdout.flush()
            time.sleep(0.3)
        print()
    
    @staticmethod
    def success_anim():
        frames = ["+", "*", "#", "@"]
        for frame in frames:
            sys.stdout.write(f"\r\033[92m{frame} TARGET HIT {frame}\033[0m")
            sys.stdout.flush()
            time.sleep(0.2)
        print()

# ==================== BANNER SYSTEM ====================
def show_banner(mode="main"):
    os.system('clear' if os.name != 'nt' else 'cls')
    
    banners = {
        "main": '''
\033[91m
    N G L   S P A M M E R
    P R E C I S I O N   E D I T I O N
\033[93m
    Exact Hits • Chat Support • Sound Effects
\033[0m''',
        
        "precision": '''
\033[92m
    P R E C I S I O N   M O D E
    100% Accuracy • Exact Hits Guaranteed
\033[0m''',
        
        "chat": '''
\033[94m
    C H A T   S U P P O R T
    Direct WhatsApp Admin Connection
\033[0m'''
    }
    
    print(banners.get(mode, banners["main"]))

# ==================== PRECISION SPAM ENGINE ====================
class Spammer:
    def __init__(self, mode="precision"):
        self.success = 0
        self.failed = 0
        self.target_count = 0
        self.lock = threading.Lock()
        self.mode = mode
        
        self.configs = {
            "precision": {"workers": 20, "delay": 0.2, "retries": 5, "timeout": 10},
            "fast": {"workers": 40, "delay": 0.05, "retries": 3, "timeout": 5},
            "stealth": {"workers": 10, "delay": 0.5, "retries": 3, "timeout": 8},
            "power": {"workers": 60, "delay": 0, "retries": 2, "timeout": 3}
        }
    
    def verify_attack(self, username):
        try:
            check_urls = [f"https://ngl.link/{username}"]
            for url in check_urls:
                try:
                    response = requests.get(url, timeout=5)
                    if response.status_code == 200:
                        return True
                except:
                    continue
        except:
            pass
        return False
    
    def send_attack(self, username, message, attack_id):
        config = self.configs[self.mode]
        
        for retry in range(config["retries"]):
            try:
                payload = {
                    'username': username,
                    'question': f"{message}",
                    'deviceId': f'device_{int(time.time()*1000)}',
                    'gameSlug': '',
                    'referrer': '',
                    'askMode': '',
                    'timestamp': int(time.time() * 1000)
                }
                
                endpoints = [
                    ('https://ngl.link/api/submit', 'json'),
                    ('https://ngl.link/api/questions', 'json'),
                    ('https://ngl.link/send', 'form')
                ]
                
                for endpoint, payload_type in endpoints:
                    try:
                        if payload_type == 'json':
                            response = requests.post(
                                endpoint,
                                json=payload,
                                timeout=config["timeout"],
                                headers={
                                    'Content-Type': 'application/json',
                                    'User-Agent': 'Mozilla/5.0'
                                }
                            )
                        else:
                            response = requests.post(
                                endpoint,
                                data=payload,
                                timeout=config["timeout"],
                                headers={
                                    'Content-Type': 'application/x-www-form-urlencoded',
                                    'User-Agent': 'Mozilla/5.0'
                                }
                            )
                        
                        if response.status_code == 200:
                            if self.verify_attack(username):
                                with self.lock:
                                    self.success += 1
                                return True
                        
                    except:
                        continue
                
            except:
                pass
            
            time.sleep(0.5 * (retry + 1))
        
        with self.lock:
            self.failed += 1
        return False
    
    def launch_attack(self, username, message, count):
        config = self.configs[self.mode]
        
        print(f"\n\033[95mPrecision Targeting Activated")
        print(f"Target: {username}")
        print(f"Message: {message}")
        print(f"Required Hits: {count}")
        print(f"Max Retries: {config['retries']}")
        print(f"Attack Threads: {config['workers']}\033[0m")
        
        Animations.precision_load(count)
        
        self.success = 0
        self.failed = 0
        self.target_count = count
        start_time = time.time()
        
        attempts = 0
        max_attempts = count * 2
        
        with ThreadPoolExecutor(max_workers=config["workers"]) as executor:
            while self.success < count and attempts < max_attempts:
                needed = count - self.success
                
                futures = []
                batch_size = min(needed, config["workers"])
                
                for i in range(batch_size):
                    attempts += 1
                    future = executor.submit(
                        self.send_attack,
                        username, message, attempts
                    )
                    futures.append(future)
                
                for future in as_completed(futures):
                    try:
                        future.result(timeout=config["timeout"])
                    except:
                        pass
                
                elapsed = time.time() - start_time
                percent = (self.success / count) * 100
                bar_length = 40
                filled = int(bar_length * self.success // count)
                bar = '#' * filled + '.' * (bar_length - filled)
                
                sys.stdout.write(
                    f"\r\033[92m[{bar}] {percent:.1f}% | "
                    f"Hits: {self.success}/{count} | "
                    f"Failed: {self.failed} | "
                    f"Time: {elapsed:.1f}s\033[0m"
                )
                sys.stdout.flush()
                
                if config["delay"] > 0:
                    time.sleep(config["delay"])
        
        total_time = time.time() - start_time
        
        if self.success >= count:
            SoundSystem.play_sound()
            Animations.success_anim()
        
        return self.success, total_time, self.failed

# ==================== CHAT SUPPORT SYSTEM ====================
class ChatSupport:
    @staticmethod
    def open_whatsapp():
        whatsapp_url = "https://wa.me/601139183035"
        print(f"\033[94mOpening WhatsApp: {whatsapp_url}\033[0m")
        
        try:
            webbrowser.open(whatsapp_url)
            print("\033[92mWhatsApp opened in browser\033[0m")
            
            print("\n\033[96mSuggested Message:")
            print("Hello admin, I need help with the spammer tool!")
            print("Please provide support when available.\033[0m")
            
            input("\n\033[93mPress ENTER to continue...\033[0m")
            
        except:
            print(f"\033[91mFailed to open WhatsApp\033[0m")
            print(f"\033[94mManual URL: {whatsapp_url}\033[0m")
    
    @staticmethod
    def show_chat_menu():
        show_banner("chat")
        
        print("\n\033[97m" + "=" * 45)
        print("           CHAT SUPPORT MENU")
        print("=" * 45)
        print("\033[94m1. Open WhatsApp Chat with Admin")
        print("2. View Support Information")
        print("3. Report Bug/Issue")
        print("4. Request Feature")
        print("5. Back to Main Menu\033[0m")
        print("\033[97m" + "=" * 45 + "\033[0m")
        
        choice = input("\n\033[95mSelect option: \033[0m")
        return choice

# ==================== MENU SYSTEM ====================
def show_main_menu():
    print("\n\033[97m" + "=" * 50)
    print("             PRECISION SPAM MENU")
    print("=" * 50)
    print("\033[92m1. PRECISION MODE - 100% Accurate")
    print("\033[96m2. FAST MODE     - Maximum Speed")
    print("\033[93m3. STEALTH MODE  - Undetectable")
    print("\033[95m4. POWER MODE    - Maximum Power")
    print("\033[94m5. CHAT SUPPORT  - WhatsApp Admin")
    print("\033[90m6. SETTINGS      - Configure Tool")
    print("\033[91m7. EXIT          - Close Program")
    print("\033[97m" + "=" * 50 + "\033[0m")
    
    choice = input("\n\033[95mSelect [1-7]: \033[0m")
    return choice

def settings_menu():
    show_banner()
    print("\n\033[96mSETTINGS MENU")
    print("1. Set Default Attack Count")
    print("2. Configure Retry Attempts")
    print("3. View Attack History")
    print("4. Clear All Logs")
    print("5. Test Sound System")
    print("6. Back to Main Menu")
    
    choice = input("\n\033[95mSelect: \033[0m")
    return choice

# ==================== MAIN FUNCTION ====================
def main():
    print("\033[96mLoading sound system...\033[0m")
    SoundSystem.play_sound()
    time.sleep(1)
    
    while True:
        show_banner("main")
        choice = show_main_menu()
        
        if choice == "7":
            print("\n\033[92mThank you for using NGL Spammer!\033[0m")
            break
        
        elif choice == "5":
            chat_system = ChatSupport()
            while True:
                chat_choice = chat_system.show_chat_menu()
                
                if chat_choice == "1":
                    chat_system.open_whatsapp()
                    break
                elif chat_choice == "5":
                    break
                else:
                    print("\033[91mFeature coming soon!\033[0m")
                    input("\nPress ENTER to continue...")
        
        elif choice == "6":
            while True:
                settings_choice = settings_menu()
                
                if settings_choice == "6":
                    break
                elif settings_choice == "5":
                    print("\033[96mTesting sound system...\033[0m")
                    SoundSystem.play_sound()
                elif settings_choice == "3":
                    if os.path.exists('attack_log.txt'):
                        with open('attack_log.txt', 'r') as f:
                            print("\n" + f.read())
                    else:
                        print("\n\033[91mNo attack logs found\033[0m")
                    input("\nPress ENTER to continue...")
        
        elif choice in ["1", "2", "3", "4"]:
            modes = {
                "1": "precision",
                "2": "fast", 
                "3": "stealth",
                "4": "power"
            }
            selected_mode = modes[choice]
            
            show_banner(selected_mode)
            
            print("\033[97m" + "-" * 45 + "\033[0m")
            link = input("\033[95mNGL Link: \033[0m").strip()
            
            if "ngl.link/" in link:
                username = link.split("ngl.link/")[1].split('?')[0].split('/')[0]
                print(f"\033[92mUsername detected: {username}\033[0m")
            else:
                username = input("\033[95mEnter username: \033[0m").strip()
            
            message = input("\033[95mMessage: \033[0m").strip()
            if not message:
                message = "Message from NGL Spammer"
            
            try:
                count = int(input("\033[95mExact number of attacks: \033[0m"))
                if count <= 0:
                    count = 50
            except:
                count = 50
            
            print("\n\033[91m" + "!" * 45)
            print(f"CONFIRMATION")
            print(f"Target: {username}")
            print(f"Message: {message[:25]}...")
            print(f"Required Hits: {count}")
            print(f"Mode: {selected_mode}")
            print("!" * 45 + "\033[0m")
            
            confirm = input("\n\033[91mConfirm launch? (y/n): \033[0m")
            if confirm.lower() != 'y':
                print("\033[91mAttack cancelled\033[0m")
                continue
            
            Animations.loading(f"Starting {selected_mode} mode")
            
            spammer = Spammer(mode=selected_mode)
            success, attack_time, failed = spammer.launch_attack(username, message, count)
            
            print(f"\n\033[92m" + "=" * 45)
            print(f"ATTACK COMPLETE")
            print(f"Successful Hits: {success}/{count}")
            
            if success >= count:
                print(f"TARGET ACHIEVED: 100% Accuracy!")
            else:
                accuracy = (success / count) * 100
                print(f"Accuracy: {accuracy:.1f}%")
            
            print(f"Failed Attempts: {failed}")
            print(f"Total Time: {attack_time:.1f} seconds")
            print(f"Attack Speed: {success/attack_time:.1f} hits/sec")
            print("=" * 45 + "\033[0m")
            
            with open('attack_log.txt', 'a') as f:
                log_entry = (
                    f"[{selected_mode}] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
                    f"Target: {username} | "
                    f"Hits: {success}/{count} | "
                    f"Failed: {failed} | "
                    f"Time: {attack_time:.1f}s\n"
                )
                f.write(log_entry)
            
            continue_choice = input("\n\033[96mLaunch another attack? (y/n): \033[0m")
            if continue_choice.lower() != 'y':
                break

# ==================== EXECUTE ====================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[91mProgram interrupted\033[0m")
    except Exception as e:
        print(f"\n\033[91mError: {str(e)}\033[0m")
    
    print("\n\033[94mNGL Spammer terminated\033[0m")
    print("\033[96mPlaying exit sound...\033[0m")
    SoundSystem.play_sound()
