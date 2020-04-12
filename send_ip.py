import urllib.request
import json

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
    msg = f'blah\nblah'
    print(msg)


if __name__ == '__main__':
    main()