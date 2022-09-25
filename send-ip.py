import urllib.request
import json
import socket
import boto3
import time

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

def localip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def main():
    session = boto3.Session(profile_name="my-ip")
    dynamodb = session.resource("dynamodb")
    table = dynamodb.Table(get_config()["table_name"])
    table.put_item(
        Item={
            "id": str(time.time()),
            "ip4Only": ip4only(),
            "myip": myip(),
            "ipify": ipify(),
            "local": localip()
        }
    )

if __name__ == '__main__':
    main()
