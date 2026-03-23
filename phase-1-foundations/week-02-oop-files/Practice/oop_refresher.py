import pandas as pd
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR,'..', '..','week-04-pandas-analysis', 'epg_schedule_20260311_041046.json')

with open (filepath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

# print(df['runtime'].head())

class Show:
    def __init__(self,title,network,runtime,airtime):
        self.title = title
        self.network = network
        self.runtime = runtime
        self.airtime = airtime

    def is_primetime(self):
        return self.airtime > '20:00'
    def is_movie(self):
        return self.runtime >= 90
    def summary(self):
        return (f"{self.title} | {self.network} | {self.runtime} mins | {self.airtime}")
    

hannity = Show('Hannity', 'Fox News Channel', 60, '21:00')
# print(hannity.title)
# print(hannity.is_primetime())
# print(hannity.is_movie())
# print(hannity.summary())


class Catalog:
    def __init__(self):
        self.shows = []
    def add_show(self,show):
        self.shows.append(show)
    def total_shows(self):
        return len(self.shows)
    def find_primetime(self):
        return [show.summary() for show in self.shows if show.is_primetime()]
    
new_catalog = Catalog()
new_show = Show('Breaking bad','ABC',60,'16:00')
new_catalog.add_show(new_show)
new_catalog.add_show(hannity)
print(new_catalog.total_shows())
print(new_catalog.find_primetime())
