from oauth2client import file, client, tools
from googleapiclient.discovery import build

def main():
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    store = file.Storage("token.json")
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets("credentials.json", "https://www.googleapis.com/auth/gmail.send")
        flags = parser.parse_args()
        creds = tools.run_flow(flow, store, flags)
        build('gmail', 'v1', http=creds.authorize(Http()))
    else:
        print("Token already exists!")


if __name__ == '__main__':
    main()