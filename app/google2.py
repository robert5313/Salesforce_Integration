#pip install google-api-python-client
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = './trans_app.json'
PARENT_FOLDER_ID = "13qsX7jqt_5BFfGDU27dWNPL0otN7wSgD"

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name' : "Demonstration",
        'parents' : [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()
#upload_json_file('test.json')
upload("tester.txt")
upload("test.json")
upload("stater.png")