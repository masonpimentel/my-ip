from oauth2client import file, client, tools
from googleapiclient.discovery import build
import argparse

def main():
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    store = file.Storage("token.json")
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets("credentials.json", "https://www.googleapis.com/auth/gmail.send")
        flags = parser.parse_args()
        tools.run_flow(flow, store, flags)
    else:
        print("Token already exists!")


if __name__ == '__main__':
    main()
