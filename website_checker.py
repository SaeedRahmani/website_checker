import requests
import hashlib
import schedule
import time
import signal
from twilio.rest import Client
from datetime import datetime

# Twilio configuration
account_sid = '---'
auth_token = '---'
twilio_whatsapp_number = 'whatsapp:+---'
recipient_whatsapp_number = 'whatsapp:+---'  # Your number

client = Client(account_sid, auth_token)

def send_whatsapp(message):
    client.messages.create(
        body=message,
        from_=twilio_whatsapp_number,
        to=recipient_whatsapp_number
    )

def get_page_content(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    return response.text

def hash_content(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def check_for_changes(url, previous_hash):
    try:
        html_content = get_page_content(url)
        current_hash = hash_content(html_content)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Current hash: {current_hash}")
        print(f"[{current_time}] Previous hash: {previous_hash}")

        if current_hash != previous_hash:
            print(f"[{current_time}] Content has changed! Sending WhatsApp message...")
            send_whatsapp("Website content changed!")
            return current_hash
        else:
            print(f"[{current_time}] No change detected.")
    except Exception as e:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Error checking for changes: {e}")
    return previous_hash

def job():
    global previous_hash
    previous_hash = check_for_changes(url, previous_hash)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Updated previous_hash: {previous_hash}")

def signal_handler(sig, frame):
    print('Exiting gracefully...')
    global stop_flag
    stop_flag = True

# Register the signal handler for graceful shutdown
signal.signal(signal.SIGINT, signal_handler)

url = "https://holland2stay.com/residences?city%5Bfilter%5D=Delft%2C26&page=1"
html_content = get_page_content(url)
previous_hash = hash_content(html_content)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"[{current_time}] Initial hash: {previous_hash}")

schedule.every(1).minute.do(job)

stop_flag = False

while not stop_flag:
    schedule.run_pending()
    time.sleep(1)

print('Script terminated.')
