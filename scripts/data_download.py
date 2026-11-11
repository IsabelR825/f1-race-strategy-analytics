import requests
import pandas as pd
from pathlib import Path 

base_url = "https://api.openf1.org/v1"
url = base_url + "/sessions"

parameters = {
    "year": 2026, 
    "country_name": "Mexico",
    "session_name": "Race"
}
#sending request to API
response = requests.get(
    url,
    params=parameters,
    timeout=30
)

#stopping if API returns an error
response.raise_for_status()

sessions = response.json() #convert into json form

#check if a matching session exists for the parameters
if not sessions:
    raise ValueError("No matching race found.")

session = sessions[0]  #get the first matching session
session_key = session["session_key"]

print("Race location:", session["location"])
print("Session:", session["session_name"])
print("Session key:", session_key)

#to store raw data
raw_folder = Path("data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)

datasets = ["drivers", "laps" , "stints", "pit", "session_result"]

#download each dataset
for dataset in datasets:
    dataset_url = base_url + "/" + dataset

    response = requests.get(dataset_url, params={"session_key": session_key}, timeout=60)

    response.raise_for_status()
    
    data = response.json()
    
    #save the data to a CSV file
    df = pd.DataFrame(data)
    df.to_csv(raw_folder / f"{dataset}.csv", index=False)

    print("Downloaded", dataset, ":", len(df), "rows")

#displaying drivers and their constructors
drivers = pd.read_csv("data/raw/drivers.csv")

#select driver names and team names 
constructors = drivers[["full_name", "team_name"]]

constructors = constructors.drop_duplicates()

constructors.to_csv(
    "data/raw/constructors.csv",
    index=False
)

print("\nDrivers and Constructors:")
print(constructors)

print("\nAll datasets downloaded successfully!")
