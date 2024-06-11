# Website Checker

The Website Checker is a Python script designed to monitor changes on a specified website. It periodically checks the website for any changes in its content. If a change is detected, the script sends a notification via WhatsApp.

## Features

- **Website Monitoring:** Automatically checks for changes in the content of a specified website.
- **WhatsApp Notifications:** Sends a WhatsApp message if a change is detected in the website's content.
- **Graceful Shutdown:** Supports graceful shutdown by handling SIGINT signal.

## Requirements

- Python 3.x
- `requests` library
- `hashlib` library
- `schedule` library
- `twilio` library

## Setup


1. Install the required Python libraries:
```sh
pip install requests schedule twilio
```
2. Configure Twilio:
    - Sign up for a Twilio account and obtain your account_sid and auth_token.
    - Set up a WhatsApp sender number and obtain the twilio_whatsapp_number.
    - Specify the recipient WhatsApp number in recipient_whatsapp_number.

3. Update the url variable in the script to the website you want to monitor.

## Usage

Run the script using Python:

```sh
python website_checker.py
```