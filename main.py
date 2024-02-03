import requests, time, random
from string import digits, ascii_lowercase
print("Made By ISellStuff")
print()

webhook = input("Enter Webhook: ")
while True:
    try:
        time.sleep(0.2)
        session = requests.Session()
        letters: str = digits + ascii_lowercase 
        username: str = "".join(random.choices(letters, k=4))
        find = requests.get(f"https://rec.net/user/{username}")
        if find.status_code == 403:
            print("[VALID USER]")
            session.post(webhook, json={'content': f"[VALID USER]: {username}"})
        if find.status_code == 200:
            print(f"[USER NOT AVAILABLE]: {username}")
            session.post(webhook, json={'content': f"[USER NOT AVAILABLE]: {username}"})
    except:
        print("[BAN]")
        session.post(webhook, json={'content': f"[BAN]"})
