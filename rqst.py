import requests
import datetime 
from tabulate import tabulate
from math import ceil


default_date = datetime.datetime.now()
events = {'depart':['departure', 'Отправление'], 'arr':['arrival', 'Прибытие']}
station_codes = {'Moscow':'s9602494', 'Finnish':'s9602497', 'Baltic':'s9602498', 'Vitebski':'s9602496', 'Ladozhski':'s9602499', 'Pulkovo':'s9600366'}
transport_types = ['plane', 'train', 'suburban']


def requesting_info( station, event, period, category, date=default_date):
    key = 'eb3a79de-1bd8-4e64-8a74-f95314d94149'
    schedule_api = f'https://api.rasp.yandex.net/v3.0/schedule/?apikey={key}&station={station}&date={str(date)}&event={event}&transport_types={category}'
    response = requests.get(schedule_api).json()
    number_of_flights = int(ceil(response['pagination']['total']/100))
    flights = []
    for i in range(number_of_flights):
        schedule_api += f'&offset={i*100}'
        response = requests.get(schedule_api).json()
        name = response['station']['station_type_name']+' '+response['station']['title']
        timesheet = response['schedule']
        for flight in timesheet:
                    info = []
                    if 0 <= datetime.datetime.fromisoformat(flight[event][:19]).hour - default_date.hour  <= period:
                        info.append(flight['thread']['number'])
                        info.append(flight['thread']['title'])
                        info.append(flight[event][11:16])
                        info.append(flight['thread']['carrier']['title'])
                        flights.append(info)
    return name, flights

def flight_table(event_type, period):
    name, flights = requesting_info(station_codes['Pulkovo'], events[event_type][0], period, transport_types[0])
    heading = f'Табло рейсов {name} на {events[event_type][1]}\n'
    table = (tabulate(flights, headers = ["№ Рейса", "Рейс", "Время", 'Авиакомпания'], tablefmt="github"))
    create_file(heading, table)

def train_table(station_name, event_type, period):
    name, flights = requesting_info(station_codes[station_name], events[event_type][0], period, transport_types[1])
    heading = (f'Расписание поездов ({name}), \n') 
    table = (tabulate(flights, headers = ["№ поезда", "Поезд", "Время", 'Перевозчик'], tablefmt="github"))
    create_file(heading, table)

def suburban_table(station_name, event_type, period):
    name, flights = requesting_info(station_codes[station_name], events[event_type][0], period, transport_types[2])
    heading = (f'Расписание Электричек ({name}), \n') 
    table = (tabulate(flights, headers = ["№", "Направление электрички", "Время", 'Перевозчик'], tablefmt="github"))
    create_file(heading, table)

def create_file(heading, table):
    f = open('schedule.txt', 'w')
    f.write(heading)
    f.write(f'\n{table}')
    f.close()
    
