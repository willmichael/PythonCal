import calendar 
import sys
import time
import fire
import os
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import datetime as dt



class PyCal():
### MARK: - Inputs

    # Update Calendar
    def u(self, date, name):
        insert_event(date, name)

    # Display day
    def d(self, *args):
        count = len(args)
        # Display today
        if count == 0:
            disp_day(0, 0)
        # Display day n
        elif count == 1:
            disp_day(args[0], args[0])
        # Display day range
        else:
            disp_day(args[0], args[1])
    
    # Next Events
    def n(self, *args):
        count = len(args)
        # Display next event
        if count == 0:
            disp_num(1)
        # Display next n events
        elif count == 1:
            disp_num(args[0])

    # Delete Events
    ### TODO: - implement

### MARK: - Insert

def insert_event(*args):
    service = auth()
    event = {}
    tod = (dt.date.today() + dt.timedelta(days=args[0])).isoformat()
    start_date = append_time(tod, 0)
    end_date = append_time(tod, 1)
    event['start'] = {'dateTime': start_date}
    event['end'] = {'dateTime': end_date}
    event['summary'] = args[1]
    event = service.events().insert(calendarId='primary', body=event).execute()
    print 'Event created: %s' % (event.get('htmlLink'))

### MARK: - Queries

# Query by number of events
def query_num(num_results):
    service = auth()
    now = dt.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='primary', 
        timeMin=now, 
        maxResults=num_results, 
        singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    return events

def disp_num(num_results):
    events = query_num(num_results)
    for e in events:
        start = e['start'].get('dateTime')
        print(start, e['summary'])


# Query by days
def query_day(day_start, day_offset):
    service = auth()

    # Init Days
    tod = (dt.date.today() + dt.timedelta(days=day_start)).isoformat()
    tod_end = (dt.date.today() + dt.timedelta(days=day_offset)).isoformat()
    today = append_time(tod, 0)
    today_end = append_time(tod_end, 24)

    # Query
    eventsResult = service.events().list(
        calendarId='primary', 
        timeMin=today, 
        timeMax=today_end, 
        maxResults=50, 
        singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    return events

def disp_day(day_start, day_offset):
    events = query_day(day_start, day_offset)
    for e in events:
        start = e['start'].get('dateTime')
        print(start, e['summary'])


### MARK: - Helper functions

# Append time beginning or time end
def append_time(date, time):
    if time == 0:
        return date + "T00:00:00.00Z"
    if time == 1:
        return date + "T01:00:00.00Z"
    else:
        return date + "T23:59:59.00Z"

# MARK: - auth

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'PyCal'

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def auth():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    return service


def main():
    fire.Fire(PyCal)

if __name__ == "__main__":
    main()

