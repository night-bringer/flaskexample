import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

relable_column_json = {'displayName':'Name', 'totalConfirmed':'Confirmed', 'totalDeaths':'Deaths', 'totalRecovered':'Recovered',
                          'totalConfirmedDelta':'Confirmed (Delta)','totalDeathsDelta':'Deaths (Delta)', 'totalRecoveredDelta':'Recovered (Delta)'}

summary_columns = ['Name','Confirmed','Recovered','Deaths','Confirmed (Delta)','Recovered (Delta)','Deaths (Delta)']

def grab_covid_stats():
    url="https://bing.com/covid/"
    rawdata=requests.get(url)
    html=rawdata.content
    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.findAll('script', attrs={'type':'text/javascript'})
    for script in scripts:
        if "var data" in script.text:
            data_extract =  script.text.replace("var data=","").strip()[:-1]
    json_data = json.loads(data_extract)
    df_country = pd.DataFrame(json_data['areas'])
    return df_country

def return_clean_covid_data():
    covid_data = grab_covid_stats()
    covid_data.rename(columns = relable_column_json, inplace = True)
    return covid_data[summary_columns]