#!/usr/bin/env python3
import os, sys, time, requests, threading, socket, platform, subprocess

P = '\033[1;35m'
W = '\033[0m'
G = '\033[1;32m'
R = '\033[31m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading():
    clear()
    bar = "████████████████████████████████████████"
    print(f"{P}[!] INITIALIZING VENOMX  KERNEL...")
    for i in range(101):
        load = bar[:i//2] + "-" * (20 - i//2)
        sys.stdout.write(f'\r{P}[{load}] {i}% COMPLETED')
        sys.stdout.flush()
        time.sleep(0.03)
    print(f"\n[+] SYSTEM ENCRYPTED. ACCESS GRANTED.{W}")
    time.sleep(1)

def banner():
    clear()
    print(f"""{P}
 █████   █████ ██████████ ██████   █████    ███████    ██████   ██████ █████ █████
▒▒███   ▒▒███ ▒▒███▒▒▒▒▒█▒▒██████ ▒▒███   ███▒▒▒▒▒███ ▒▒██████ ██████ ▒▒███ ▒▒███
 ▒███    ▒███  ▒███  █ ▒  ▒███▒███ ▒███  ███     ▒▒███ ▒███▒█████▒███  ▒▒███ ███
 ▒███    ▒███  ▒██████    ▒███▒▒███▒███ ▒███      ▒███ ▒███▒▒███ ▒███   ▒▒█████
 ▒▒███   ███   ▒███▒▒█    ▒███ ▒▒██████ ▒███      ▒███ ▒███ ▒▒▒  ▒███    ███▒███
  ▒▒▒█████▒    ▒███ ▒   █ ▒███  ▒▒█████ ▒▒███     ███  ▒███      ▒███   ███ ▒▒███
    ▒▒███      ██████████ █████  ▒▒█████ ▒▒▒███████▒   █████     █████ █████ ████
     ▒▒▒      ▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒▒▒    ▒▒▒▒▒     ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒
              [ THE WEB DEEP HUNTER | VERSION 4.0 ]
              [ STATUS: PURPLE ARSENAL | BY: Anonymous40443 ]
    {W}""")

def web_fuzzer(target, wordlist):
    print(f"\n{P}[*] TARGETING DIRECTORIES: {target}{W}")
    if not os.path.exists(wordlist):
        print(f"{R}[!] WORDLIST NOT FOUND!{W}")
        return
    try:
        with open(wordlist, 'r') as f:
            paths = f.read().splitlines()
        def check(path):
            url = f"{target}/{path}" if target.endswith('/') else f"{target}/{path}"
            try:
                r = requests.get(url, timeout=2)
                if r.status_code == 200: print(f"{G}[FOUND] {url} (200 OK){W}")
                elif r.status_code == 403: print(f"{R}[FORBIDDEN] {url} (403){W}")
            except: pass
        for p in paths:
            t = threading.Thread(target=check, args=(p,))
            t.start()
            time.sleep(0.05)
    except Exception as e: print(f"{R}[!] ERROR: {e}{W}")

def ghost_ip(target):
    print(f"\n{P}[*] TRACING TARGET INFO...{W}")
    try:
        clean_target = target.replace("http://","").replace("https://","").split('/')[0]
        ip = socket.gethostbyname(clean_target)
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(f"{P}IP: {ip}\nCITY: {r.get('city')}\nISP: {r.get('isp')}\nASN: {r.get('as')}{W}")
    except: print(f"{R}[!] TRACE FAILED.{W}")

def armor_audit(target):
    print(f"\n{P}[*] AUDITING SECURITY HEADERS...{W}")
    try:
        r = requests.get(target)
        h = r.headers
        score = 0
        checks = ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options', 'X-Content-Type-Options']
        for c in checks:
            if c in h:
                print(f"{G}[+] {c}: PROTECTED{W}")
                score += 25
            else:
                print(f"{R}[- ] {c}: VULNERABLE (MISSING){W}")
        print(f"\n{P}FINAL SECURITY SCORE: {score}/100{W}")
    except: print(f"{R}[!] AUDIT FAILED.{W}")

def main():
    loading()
    while True:
        banner()
        print(f"1 - {P}[ FUZZER ] Deep Path Discovery{W}")
        print(f"2 - {P}[ GHOST-IP ] OSINT & IP Tracker{W}")
        print(f"3 - {P}[ ARMOR ] Security Audit{W}")
        print(f"4 - {P}[ SETUP ] Install Wordlists{W}")
        print(f"0 - {R}EXIT{W}")
        
        op = input(f"\n{P}VENOMX:~$ {W}")
        if op == '1':
            t = input(f"{P}Target URL: {W}")
            w = input(f"{P}Wordlist Path (common.txt): {W}")
            web_fuzzer(t, w if w else "common.txt")
            input("\nENTER to return...")
        elif op == '2':
            t = input(f"{P}Domain/IP: {W}")
            ghost_ip(t)
            input("\nENTER to return...")
        elif op == '3':
            t = input(f"{P}URL: {W}")
            armor_audit(t)
            input("\nENTER to return...")
        elif op == '4':
            print(f"{P}[*] Downloading wordlists...{W}")
            subprocess.run("curl -L https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt -o common.txt", shell=True)
            print(f"{G}[✓] READY!{W}")
            time.sleep(2)
        elif op == '0': sys.exit()

if __name__ == "__main__":
    main()
