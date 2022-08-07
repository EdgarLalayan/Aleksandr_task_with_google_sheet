from __future__ import print_function
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import time
import csv
from scraperV2 import get_full_data
from selenium.webdriver.support.ui import WebDriverWait
from scraperV1 import get_full_data


SAMPLE_RANGE_NAME = 'data!A2:B:'

class GoogleSheet:
    SPREADSHEET_ID = '1v30VB7Nhsf_RdG52fFczfE0xyuRtooXUz8Za-hR61P0'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    '/Users/edgarlalayan/Desktop/Upwork/credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def updateRangeValues(self, range, values):
        data = [{
            'range': range,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=body).execute()
        print('{0} cells updated.'.format(result.get('totalUpdatedRows')))

        
def main():
    gs = GoogleSheet()

    list_result_data= get_full_data()
    test_range = f'data!A2:C{len(list_result_data)+1}'

    gs.updateRangeValues(test_range, list_result_data)
if __name__ == '__main__':
    main()
