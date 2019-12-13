#Pomniejsze
from __future__ import print_function
import datetime
from datetime import time
import pickle
import os.path

#flask
from flask_login import current_user
from flask import request, redirect, url_for

#google
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#Daty
now = datetime.datetime.now()
now_date = now.strftime("%d-%m-%Y")
now_date1 = now.strftime("%Y:%m:%d")
now_time = now.strftime("%H:%M:%S")
now_hour = now.strftime("%H")
now_day = now.strftime("%d")

SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None

if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('calendar', 'v3', credentials=creds)

def events(day12):  
    #lista wydarzen 
    #day12 oznacza ile dni w przód ma wyszukiwać wydarzeń

    start1 = [] # data rozpoczecia wydzarzenia
    summary = [] # tytuł wydarzenia
    list1 = 0 # ilość wydarzeń
     
    if day12 == False: # wczytuje wydarzenia now + 10 h
        now = datetime.datetime.now()

        format = "%d-%m-%Y"
        #start_date = now.strptime(now_date, format)
        #end_date = start_date + datetime.timedelta(hours=24)

        start_date = now.strptime(now_date, format)
        time_to = start_date + now.strftime("%H")
        end_date = start_date + datetime.timedelta(hours=24)



        start_date = start_date.isoformat() + "Z"
        end_date = end_date.isoformat() + "Z"

        print("start", start_date)
        print("time to ", time_to)
        print("end", end_date)

        events_result = service.events().list(calendarId='primary', timeMin=start_date, timeMax=end_date, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

    else: # wczytuje wydarzenia o odpowiedznie dacie podanej w day12
        now = datetime.datetime.now()
        day1 = datetime.datetime.utcnow() + datetime.timedelta(days=int(day12))
        day1 = day1 - datetime.timedelta(hours=int(now.strftime("%H")))
        day1 = day1.isoformat() + 'Z'

        now_24 = datetime.datetime.utcnow() + datetime.timedelta(hours=12)
        now_24 = now_24 + datetime.timedelta(days=day12)
        now_24 = now_24.isoformat() + 'Z'
        
        events_result = service.events().list(calendarId='primary', timeMin=day1,timeMax=now_24, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])
    
    if not events:
        list1 = False # jeśli nie ma wydzrzeń zwraca False

    for event in events:
        letters = []
        str1 = []

        start = event['start'].get('dateTime', event['start'].get('date'))

        if event['summary'] == 'Wolne':
            len1 = list(start)
            for x in range(len(start)):
                letters.append(len1[x])

            #usuwanie niepotrzebnych znaków
            letters.pop(10)
            for x in range(9):
                letters.pop(15)

            letters.insert(10, "  -  ")
            str1 = ''.join(letters)

            summary.append(event['summary'])
            start1.append(str(str1))
            list1+=1

    return summary, start1, list1

def admin_free_events():
    # zwraca wolne terminy

    summary = [] # tytuł wydarzenia
    start1 = [] # data rozpoczecia wydzarzenia
    list2 = 0  # ilość wydarzeń

    #uzyskiwanie wydarzeń z google callendar
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    if not events:
        list2 = False

    for event in events:
        letters = []
        str1 = []
        start = event['start'].get('dateTime', event['start'].get('date'))

        if event['summary'] == 'Wolne':
            len1 = list(start)
            for x in range(len(start)):
                letters.append(len1[x])

            #usuwanie niepotrzebnych znaków
            letters.pop(10)
            for x in range(9):
                letters.pop(15)

            letters.insert(10, "  -  ")
            str1 = ''.join(letters)

            summary.append(event['summary'])
            start1.append(str(str1)) #start
            list2+=1

    return summary, start1, list2

def awaiting_events():
    #zwraca wszystkie wydarzenia oczekujące potwierdzenia
    #funkcja używana tylko w /admin

    start1 = [] # data rozpoczecia wydzarzenia
    summary = [] # tytuł wydarzenia
    desc1 = [] # opis wydarzenia
    list2 = 0  # ilość wydarzeń

    #uzyskiwanie wydarzeń z google callendar
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    if not events:
        list2 = False

    for event in events:
        letters = []
        str1 = [] 
        
        start = event['start'].get('dateTime', event['start'].get('date'))
        desc = event.get('description', 'brak danych użytkownika')

        if event['summary'] == 'Oczekujące':
            len1 = list(start)
            for x in range(len(start)):
                letters.append(len1[x])

            #usuwanie niepotrzebnych znaków
            letters.pop(10)
            for x in range(9):
                letters.pop(15)

            letters.insert(10, "  -  ")
            str1 = ''.join(letters)

            summary.append(event['summary'])
            desc1.append(desc)
            start1.append(str(str1)) #start
            list2+=1

    return summary, start1, list2, desc1

def get_desc(start_date_confirm):
    #zwraca opis wydarzenia bazując na dacie rozpoczęcia

    start1 = [] # data rozpoczecia wydzarzenia
    desc1 = [] # opis wydarzenia

    #uzyskiwanie wydarzeń z google callendar
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        letters = []
        str1 = []

        start = event['start'].get('dateTime', event['start'].get('date'))
        desc = event.get('description', 'brak danych użytkownika')

        if event['summary'] == 'Oczekujące':
            len1 = list(start)
            for x in range(len(start)):
                letters.append(len1[x])

            #usuwanie niepotrzebnych znaków
            letters.pop(10)
            for x in range(9):
                letters.pop(15)

            letters.insert(10, "  -  ")
            str1 = ''.join(letters)
            if start_date_confirm == str1:
                desc1.append(desc)
                start1.append(str(str1)) #start

    return start1, desc1

def admin_events():
    #zwraca listę zaakceptowanych wydarzeń

    start1 = [] # data rozpoczecia wydzarzenia
    summary = [] # tytuł wydarzenia
    desc1 = [] # opis wydarzenia
    list2 = 0 # ilość wydarzeń

    #uzyskiwanie wydarzeń z google callendar
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    if not events:
        list2 = False

    for event in events:
        if event['summary'] == 'Zatwierdzone':
            letters = []
            str1 = []

            start = event['start'].get('dateTime', event['start'].get('date'))
            desc = event.get('description', 'brak danych urzytkownika, ')

            len1 = list(start)
            for x in range(len(start)):
                letters.append(len1[x])

            #usuwanie niepotrzebnych znaków
            letters.pop(10)
            for x in range(9):
                letters.pop(15)

            letters.insert(10, "  -  ")
            str1 = ''.join(letters)

            summary.append(event['summary'])
            desc1.append(desc)
            start1.append(str(str1)) #start
            list2+=1
        

    return summary, start1, list2, desc1

def add_events():
    #Dodaje jedno wydarzenie teraz + 15 min
    #nie jest wykorzystane na stronie 

    now = datetime.datetime.utcnow()
    now1 = now + datetime.timedelta(minutes=15)
    # dodawanie wydarzenia do google calendar
    event = {'summary': 'Masaż', 'description': str(current_user), 'start': {'dateTime': str(now.isoformat() + 'Z')}, 'end': {'dateTime': str(now1.isoformat() + 'Z')}}
    event = service.events().insert(calendarId='primary', body=event).execute()

def update_event(start_date_confirm):
    #aktualizuje wydarzenie bazując na dacie rozpoczęcia (start_date_confirm)
    #zmienia nazwę z "Wolne" na "Oczekujące"
    #użytkownik używa tej funkcji
    
    #uzyskiwanie wydarzeń z google callendar
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        if event['summary'] == 'Wolne':
            letters = []
            str1 = []

            start = event['start'].get('dateTime', event['start'].get('date'))
            desc = event.get('description', 'brak opisu')

            len1 = list(start)
            for x in range(len(start)):
                letters.append(len1[x])

            #usuwanie niepotrzebnych znaków
            letters.pop(10)
            for x in range(9):
                letters.pop(15)

            letters.insert(10, "  -  ")
            str1 = ''.join(letters)
            if str1 == start_date_confirm:
                event_result = service.events().patch(calendarId='primary',eventId=event['id'],body={"summary": 'Oczekujące',"description":str(current_user)},).execute()
        
def update_event_admin(start_date_confirm):
    #aktualizuje wydarzenie bazując na dacie rozpoczęcia (start_date_confirm)
    #zmienia nazwę z "Oczekujące" na "Zatwierdzone"
    #admin używa tej funkcji
     
    start_date_update = start_date_confirm.pop(0)  #przekazuje wartość z confirm_admin2 do confirm_admin3

    #uzyskiwanie wydarzeń z google callendar
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
        if event['summary'] == 'Oczekujące':
            str1 = []
            letters = []
            start = event['start'].get('dateTime', event['start'].get('date'))
            desc = event.get('description', 'brak danych urzytkownika')

            len1 = list(start)
            for x in range(len(start)):
                letters.append(len1[x])

            #usuwanie niepotrzebnych znaków
            letters.pop(10)
            for x in range(9):
                letters.pop(15)

            letters.insert(10, "  -  ")
            str1 = ''.join(letters)
            if str1 == start_date_update:
                print('succes', str1)
                event_result = service.events().patch(calendarId='primary',eventId=event['id'],body={"summary": 'Zatwierdzone',},).execute()

def multi_add_events(start_date, start_time1, end_time1, len1):
    #Seryjnie dodaje wydarzenia
    #start_date data rozpoczęcia wydarzenia
    #start_time1 godzina rozpoczęcia wydarzenia
    #end_time1 godzina zakączenia wydarzenia
    #len1 długość wydarzenia

    #obliczenie ilosci loop
    now12 = datetime.datetime.now()
    loop = int(end_time1) - int(start_time1)
    loop *= 60
    loop =  int(loop) / int(len1)

    #roznica godzin
    new_target_hour = int(start_time1) - int(now_hour)

    format = "%Y-%m-%d"
    start_date = now.strptime(start_date, format)
    start_date = start_date + datetime.timedelta(hours=int(start_time1))
    start_date = start_date - datetime.timedelta(hours=2)

    end_time2 = start_date + datetime.timedelta(minutes=int(len1))
    end_time3 = end_time2.strftime("%H")

    #dodawanie wydarzen
    for x in range(int(loop)):
        end_time3 = end_time2.strftime("%H")
        if int(end_time3) == int(end_time1):
            break

        event = {'summary': 'Wolne', 'start': {'dateTime': str(start_date.isoformat() + 'Z')}, 'end': {'dateTime': str(end_time2.isoformat() + 'Z')}}
        event = service.events().insert(calendarId='primary', body=event).execute()

        start_date += datetime.timedelta(minutes=int(len1))
        end_time2 += datetime.timedelta(minutes=int(len1))

def last_events(date):

    list1 = 0 # ilość wydarzeń
    time1 = date * 24
    now = datetime.datetime.utcnow().isoformat() + 'Z' 
    now_last = datetime.datetime.now() - datetime.timedelta(hours=time1)
    now_last = now_last.isoformat() + 'Z'

    events_result = service.events().list(calendarId='primary', timeMin=now_last,timeMax=now, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    if not events:
        list1 = False

    list1 = len(events)
    return list1
