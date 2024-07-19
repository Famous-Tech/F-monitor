import requests
import time
import sys
import os
import subprocess

def animate_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def ping_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"\033[92m[{time.ctime()}] Ping to {url} successful\033[0m")
        else:
            print(f"\033[91m[{time.ctime()}] Ping to {url} failed with status code: {response.status_code}\033[0m")
    except requests.RequestException as e:
        print(f"\033[91m[{time.ctime()}] Error pinging {url}: {e}\033[0m")

def main():
    if len(sys.argv) != 2:
        print("Usage: python f-monitor.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    animate_text("""
    dev : Famous-Tech
    Info : Monitor for whattsapp bot
    Tips : Follow me on GitHub and star  this script
    """)

    print(f"Starting F-Monitor to ping {url} every minute")

    # Schedule the script to run every minute
    subprocess.run(["termux-job-scheduler", "-s", __file__, "--period", "60", "--url", url])

    while True:
        ping_url(url)
        time.sleep(60)

if __name__ == "__main__":
    main()
