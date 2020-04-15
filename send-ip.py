import urllib.request
import json
import base64
from email.message import EmailMessage
from oauth2client import file, client, tools
from googleapiclient.discovery import build

def get_config():
    with open("config.json") as config_file:
        return json.load(config_file)

# http://ip4only.me/api/
def ip4only():
    res = urllib.request.urlopen('http://ip4only.me/api/').read()
    # IPv4,64.46.13.58,Remaining fields reserved for future use,,,
    return str(res).split(",")[1]

# https://api.myip.com/
def myip():
    res = urllib.request.urlopen('https://api.myip.com/').read()
    # {"ip":"64.46.13.58","country":"Canada","cc":"CA"}
    return json.loads(res)["ip"]


# http://api.ipify.org/
def ipify():
    res = urllib.request.urlopen('http://api.ipify.org/').read()
    # '64.46.13.58'
    return res.decode()

def main():
    msg = ""
    
    try:
        msg += f"ip4only: {ip4only()}"
        msg += "\n"
    except:
        msg += "ip4only failed"
        msg += "\n"

    try:
        msg += f"myip: {myip()}"
        msg += "\n"
    except:
        msg += "myip failed"
        msg += "\n"

    try:
        msg += f"ipify: {ipify()}"
        msg += "\n"
    except:
        msg += "ipify failed"
        msg += "\n"

    email_msg = EmailMessage()
    email_msg['From'] = config_get_sender_gmail()
    email_msg['To'] = get_config()["target_email"]
    email_msg['Subject'] = get_config()["email_subject"]
    email_msg.set_content(msg)
    email_msg = {'raw': base64.urlsafe_b64encode(msg.as_string().encode()).decode()}

    store = file.Storage('token.json')
    creds = store.get()
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    try:
        message = (service.users().messages().send(userId='me', body=msg).execute())
        print(f'Sending message ID: {message['id']}'
    except errors.HttpError as e:
        print(f'An error occurred: {e}')
        raise e

if __name__ == '__main__':
    main()