#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time
import os
import sys
import json
import random
from datetime import datetime
import threading

# ============================================
# WORMGPT V5 - RERE EDITION
# GUA MUSANG KELANTAN LEAGUES
# ============================================

# COLOR POWER - RERE STYLE
R = '\033[91m'     # Merah
G = '\033[92m'     # Hijau
Y = '\033[93m'     # Kuning
B = '\033[94m'     # Biru
P = '\033[95m'     # Ungu
C = '\033[96m'     # Cyan
W = '\033[0m'      # Putih
BL = '\033[30m'    # Hitam
BG_R = '\033[41m'  # Background Merah
BG_G = '\033[42m'  # Background Hijau
BG_Y = '\033[43m'  # Background Kuning
BG_B = '\033[44m'  # Background Biru
BG_P = '\033[45m'  # Background Ungu
BG_C = '\033[46m'  # Background Cyan
BOLD = '\033[1m'   # Bold
BLINK = '\033[5m'  # Kedip-kedip
REV = '\033[7m'    # Reverse

# ============================================
# GLOBAL
# ============================================
bot_token = ""
bot_username = ""
bot_name = ""
loading = False
target_default = "601139183035"

# ============================================
# CLEAR
# ============================================
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

# ============================================
# ANIMASI BARU - RERE STYLE (LAJU)
# ============================================
def animasi_bot():
    frames = [
        f"{R}◴{W}",
        f"{Y}◵{W}",
        f"{G}◶{W}",
        f"{C}◷{W}"
    ]
    
    while loading:
        for frame in frames:
            if not loading:
                break
            sys.stdout.write(f"\r{C}[BOT]{W} SCANNING {frame} {R}⚡{W}")
            sys.stdout.flush()
            time.sleep(0.1)

def animasi_hack():
    frames = [
        f"{R}██▒▒▒▒▒▒ 20%{W}",
        f"{Y}████▒▒▒▒ 40%{W}",
        f"{G}██████▒▒ 60%{W}",
        f"{C}████████ 80%{W}",
        f"{P}██████████ 100%{W}"
    ]
    
    while loading:
        for frame in frames:
            if not loading:
                break
            sys.stdout.write(f"\r{R}[HACK]{W} BYPASS {frame}")
            sys.stdout.flush()
            time.sleep(0.1)

def animasi_spam():
    symbols = ["➤", "✦", "✧", "★", "☆", "✪", "✫", "✬", "✭", "✮", "✯"]
    
    while loading:
        for sym in symbols:
            if not loading:
                break
            sys.stdout.write(f"\r{Y}{sym} {W}FIRING {Y}{sym}{W}")
            sys.stdout.flush()
            time.sleep(0.05)

def start_animasi(jenis='bot'):
    global loading
    loading = True
    if jenis == 'bot':
        t = threading.Thread(target=animasi_bot)
    elif jenis == 'hack':
        t = threading.Thread(target=animasi_hack)
    else:
        t = threading.Thread(target=animasi_spam)
    t.daemon = True
    t.start()
    return t

def stop_animasi():
    global loading
    loading = False
    time.sleep(0.2)
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()

# ============================================
# BANNER RERE POWER
# ============================================
def banner_rere():
    clear()
    print(f"{R}{BOLD}")
    print("    ╔════════════════════════════════════════════╗")
    print("    ║  ██████╗ ███████╗██████╗ ███████╗        ║")
    print("    ║  ██╔══██╗██╔════╝██╔══██╗██╔════╝        ║")
    print("    ║  ██████╔╝█████╗  ██████╔╝█████╗          ║")
    print("    ║  ██╔══██╗██╔══╝  ██╔══██╗██╔══╝          ║")
    print("    ║  ██║  ██║███████╗██║  ██║███████╗        ║")
    print("    ║  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝        ║")
    print(f"    ╠════════════════════════════════════════════╣{W}")
    print(f"    ║{C}{BOLD}         ✦  ℝ𝔼ℝ𝔼 𝔼𝔻𝕀𝕋𝕀𝕆ℕ  ✦           {R}║{W}")
    print(f"    ║{G}       𝕋𝕆𝕆𝕃𝕊 𝔹𝕐 𝕄𝔸ℕ 𝕂𝔼𝕃𝔸𝕋𝔼              {R}║{W}")
    print(f"    ║{Y}       🏴  𝕂𝔼𝕃𝔸ℕ𝕋𝔸ℕ 𝕃𝔼𝔸𝔾𝕌𝔼𝕊  🏴           {R}║{W}")
    print(f"    ╚════════════════════════════════════════════╝{W}")
    print(f"\n{P}{BOLD}    ──── ✦ ──── ✦ ──── ✦ ──── ✦ ────{W}")
    print(f"    {Y}📞 DEFAULT TARGET: {C}{BLINK}+6{target_default}{W}")
    print(f"    {P}──── ✦ ──── ✦ ──── ✦ ──── ✦ ────{W}\n")

def banner_serang():
    print(f"\n{R}{BOLD}╔════════════════════════════════════════════╗{W}")
    print(f"{R}║{Y}          ⚔️  𝕊𝔼ℝ𝔸ℕ𝔾𝔸ℕ 𝔹𝔼ℝ𝕄𝕌𝕃𝔸  ⚔️           {R}║{W}")
    print(f"{R}║{G}          ✦  𝕄𝔸ℕ 𝕂𝔼𝕃𝔸𝕋𝔼 𝕆ℕ 𝕋𝕆ℙ  ✦          {R}║{W}")
    print(f"{R}║{C}              ➤ +6{target_default} ◀               {R}║{W}")
    print(f"{R}╚════════════════════════════════════════════╝{W}\n")

# ============================================
# CHECK TOKEN (CEPAT)
# ============================================
def check_token(token):
    global bot_username, bot_name
    url = f"https://api.telegram.org/bot{token}/getMe"
    
    t = start_animasi('hack')
    try:
        res = requests.get(url, timeout=10).json()
        stop_animasi()
        if res.get("ok"):
            bot_name = res["result"]["first_name"]
            bot_username = res["result"]["username"]
            return True, f"{G}✓ VALID{W}"
        else:
            return False, f"{R}✗ INVALID{W}"
    except:
        stop_animasi()
        return False, f"{R}✗ ERROR{W}"

# ============================================
# CEK GAMBAR
# ============================================
def cek_gambar(url):
    ok = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    for ext in ok:
        if ext in url.lower():
            return True
    return False

# ============================================
# MENU 1 - UPLOAD
# ============================================
def menu_upload(token):
    clear()
    print(f"{C}{BOLD}┌────────────────────────────────────┐{W}")
    print(f"{C}│{Y}         📸 UPLOAD GAMBAR           {C}│{W}")
    print(f"{C}└────────────────────────────────────┘{W}\n")
    
    print(f"{G}✦ LINK SUPPORT:{W}")
    print(f"  {B}• iili.io")
    print(f"  • catbox.moe")
    print(f"  • imgur.com{W}\n")
    
    url = input(f"{Y}➤ LINK: {W}").strip()
    
    if not cek_gambar(url):
        print(f"{R}✗ FORMAT SALAH!{W}")
        return
    
    cap = input(f"{Y}➤ CAPTION [ENTER SKIP]: {W}").strip()
    target = input(f"{Y}➤ CHAT ID [ENTER DEFAULT]: {W}").strip()
    
    if not target:
        target = target_default
        print(f"{C}  ➤ GUNA {target}{W}")
    
    print(f"\n{P}✦ SENDING...{W}")
    
    t = start_animasi('spam')
    try:
        api = f"https://api.telegram.org/bot{token}/sendPhoto"
        data = {
            "chat_id": target,
            "photo": url,
            "caption": cap if cap else "📸 TOOLS BY MAN KELATE"
        }
        
        res = requests.post(api, data=data, timeout=30)
        stop_animasi()
        
        if res.status_code == 200:
            print(f"\n{G}✓ BERJAYA DIHANTAR!{W}")
            print(f"  {C}➤ TARGET: {target}")
            print(f"  ➤ MASA: {datetime.now().strftime('%H:%M:%S')}{W}")
        else:
            print(f"\n{R}✗ GAGAL! CODE: {res.status_code}{W}")
    except:
        stop_animasi()
        print(f"\n{R}✗ ERROR!{W}")

# ============================================
# MENU 2 - SPAM (BARU)
# ============================================
def menu_spam(token):
    clear()
    print(f"{R}{BOLD}┌────────────────────────────────────┐{W}")
    print(f"{R}│{Y}         💣 SPAM BERTALU           {R}│{W}")
    print(f"{R}└────────────────────────────────────┘{W}\n")
    
    target = input(f"{Y}➤ CHAT ID [ENTER DEFAULT]: {W}").strip()
    if not target:
        target = target_default
        print(f"{C}  ➤ GUNA {target}{W}")
    
    print(f"\n{G}✦ TYPE MESSAGE (KETIK 'STOP' UNTUK HABIS):{W}")
    msgs = []
    while True:
        msg = input(f"{C}  MSG➤ {W}")
        if msg.upper() == 'STOP':
            break
        if msg.strip():
            msgs.append(msg)
    
    if not msgs:
        print(f"{R}✗ MESEJ KOSONG!{W}")
        return
    
    try:
        total = int(input(f"{Y}➤ JUMLAH (MAX 500): {W}"))
        total = min(total, 500)
    except:
        print(f"{R}✗ GUNA NOMBOR!{W}")
        return
    
    delay = input(f"{Y}➤ DELAY [0.1]: {W}").strip()
    delay = float(delay) if delay else 0.1
    
    banner_serang()
    time.sleep(1)
    
    api = f"https://api.telegram.org/bot{token}/sendMessage"
    success = 0
    failed = 0
    
    print(f"\n{C}✦ HASIL TEMBAKAN:{W}\n")
    
    for i in range(1, total + 1):
        try:
            text = random.choice(msgs)
            
            res = requests.post(api, data={
                "chat_id": target,
                "text": f"{text}"
            }, timeout=10)
            
            if res.status_code == 200:
                success += 1
                mark = f"{G}✓{W}"
            else:
                failed += 1
                mark = f"{R}✗{W}"
            
            print(f"  {mark} [{i:03d}] {text[:30]}")
            
            if i % 15 == 0:
                print(f"  {Y}────────── {i}/{total} ──────────{W}")
            
            time.sleep(delay)
            
        except:
            failed += 1
            print(f"  {R}✗ [{i:03d}] ERROR{W}")
    
    print(f"\n{Y}══════════════════════════════{W}")
    print(f"{G}  ✓ BERJAYA : {success:03d}{W}")
    print(f"{R}  ✗ GAGAL   : {failed:03d}{W}")
    print(f"{C}  ➤ TOTAL   : {total:03d}{W}")
    print(f"{Y}══════════════════════════════{W}")

# ============================================
# MENU 3 - NAMA
# ============================================
def menu_nama(token):
    clear()
    print(f"{G}{BOLD}┌────────────────────────────────────┐{W}")
    print(f"{G}│{C}         📝 TUKAR NAMA BOT         {G}│{W}")
    print(f"{G}└────────────────────────────────────┘{W}\n")
    
    baru = input(f"{Y}➤ NAMA BARU: {W}").strip()
    if not baru:
        print(f"{R}✗ KOSONG!{W}")
        return
    
    api = f"https://api.telegram.org/bot{token}/setMyName?name={baru}"
    
    t = start_animasi('spam')
    try:
        res = requests.get(api).json()
        stop_animasi()
        
        if res.get("ok"):
            print(f"\n{G}✓ NAMA → {baru}{W}")
        else:
            print(f"\n{R}✗ GAGAL!{W}")
    except:
        stop_animasi()
        print(f"\n{R}✗ ERROR!{W}")

# ============================================
# MENU 4 - USERNAME
# ============================================
def menu_user(token):
    clear()
    print(f"{B}{BOLD}┌────────────────────────────────────┐{W}")
    print(f"{B}│{Y}         👤 TUKAR USERNAME         {B}│{W}")
    print(f"{B}└────────────────────────────────────┘{W}\n")
    
    baru = input(f"{Y}➤ USERNAME BARU (tanpa @): {W}").strip()
    if not baru:
        print(f"{R}✗ KOSONG!{W}")
        return
    
    api = f"https://api.telegram.org/bot{token}/setUsername?username={baru}"
    
    t = start_animasi('spam')
    try:
        res = requests.get(api).json()
        stop_animasi()
        
        if res.get("ok"):
            print(f"\n{G}✓ USERNAME → @{baru}{W}")
        else:
            print(f"\n{R}✗ GAGAL! {res.get('description', '')}{W}")
    except:
        stop_animasi()
        print(f"\n{R}✗ ERROR!{W}")

# ============================================
# MENU 5 - BIO
# ============================================
def menu_bio(token):
    clear()
    print(f"{P}{BOLD}┌────────────────────────────────────┐{W}")
    print(f"{P}│{G}         📋 TUKAR BIO BOT          {P}│{W}")
    print(f"{P}└────────────────────────────────────┘{W}\n")
    
    baru = input(f"{Y}➤ BIO BARU: {W}").strip()
    if not baru:
        print(f"{R}✗ KOSONG!{W}")
        return
    
    api = f"https://api.telegram.org/bot{token}/setMyDescription?description={baru}"
    
    t = start_animasi('spam')
    try:
        res = requests.get(api).json()
        stop_animasi()
        
        if res.get("ok"):
            print(f"\n{G}✓ BIO DITUKAR!{W}")
        else:
            print(f"\n{R}✗ GAGAL!{W}")
    except:
        stop_animasi()
        print(f"\n{R}✗ ERROR!{W}")

# ============================================
# MENU 6 - INFO
# ============================================
def menu_info(token):
    clear()
    print(f"{C}{BOLD}┌────────────────────────────────────┐{W}")
    print(f"{C}│{P}         ℹ️  INFO BOT             {C}│{W}")
    print(f"{C}└────────────────────────────────────┘{W}\n")
    
    api = f"https://api.telegram.org/bot{token}/getMe"
    
    t = start_animasi('bot')
    try:
        res = requests.get(api).json()
        stop_animasi()
        
        if res.get("ok"):
            d = res["result"]
            print(f"{G}┌────────────────────────────┐{W}")
            print(f"{G}│{C} NAMA   : {d['first_name']}{W}")
            print(f"{G}│{C} USER   : @{d['username']}{W}")
            print(f"{G}│{C} ID     : {d['id']}{W}")
            print(f"{G}│{C} STATUS : {G}✓ AKTIF{W}")
            print(f"{G}└────────────────────────────┘{W}")
        else:
            print(f"{R}✗ TAK DAPAT INFO{W}")
    except:
        stop_animasi()
        print(f"{R}✗ ERROR{W}")

# ============================================
# MAIN
# ============================================
def main():
    global bot_token
    
    while True:
        banner_rere()
        
        if not bot_token:
            token = input(f"{Y}➤ BOT TOKEN: {W}").strip()
            status, msg = check_token(token)
            
            if status:
                bot_token = token
                print(f"\n{G}✓ BOT: {bot_name} (@{bot_username}){W}")
                print(f"{C}✓ DEFAULT: +6{target_default}{W}\n")
                time.sleep(1)
            else:
                print(f"\n{R}✗ TOKEN TAK SAH!{W}")
                input(f"\n{Y}TEK ENTER...{W}")
                continue
        
        # MENU RERE
        print(f"{C}{BOLD}┌────────────────────────────────────┐{W}")
        print(f"{C}│{Y}         𝕄𝔼ℕ𝕌 ℝ𝔼ℝ𝔼                {C}│{W}")
        print(f"{C}├────────────────────────────────────┤{W}")
        print(f"{C}│{G}  [1]{W}  📸 UPLOAD GAMBAR              {C}│{W}")
        print(f"{C}│{R}  [2]{W}  💣 SPAM ATTACK                {C}│{W}")
        print(f"{C}│{Y}  [3]{W}  📝 TUKAR NAMA                 {C}│{W}")
        print(f"{C}│{B}  [4]{W}  👤 TUKAR USERNAME             {C}│{W}")
        print(f"{C}│{P}  [5]{W}  📋 TUKAR BIO                  {C}│{W}")
        print(f"{C}│{C}  [6]{W}  ℹ️  INFO BOT                  {C}│{W}")
        print(f"{C}│{R}  [7]{W}  ❌ KELUAR                     {C}│{W}")
        print(f"{C}└────────────────────────────────────┘{W}\n")
        
        pilih = input(f"{G}PILIH {R}➤ {W}").strip()
        
        if pilih == '1':
            menu_upload(bot_token)
        elif pilih == '2':
            menu_spam(bot_token)
        elif pilih == '3':
            menu_nama(bot_token)
        elif pilih == '4':
            menu_user(bot_token)
        elif pilih == '5':
            menu_bio(bot_token)
        elif pilih == '6':
            menu_info(bot_token)
        elif pilih == '7':
            print(f"\n{Y}✦ DAAAH... JUMPA LAGI BOSS ✦{W}")
            print(f"{C}✦ MAN KELATE LEAGUES ✦{W}")
            time.sleep(1)
            clear()
            sys.exit(0)
        else:
            print(f"{R}✗ PILIH 1-7 JE!{W}")
        
        input(f"\n{Y}➤ TEK ENTER...{W}")

# ============================================
# JALAN
# ============================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Y}✦ BYE BYE! ✦{W}")
        sys.exit(0)
