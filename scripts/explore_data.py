import pandas as pd

#loads lap data
laps = pd.read_csv("data/raw/laps.csv")

#display firsts 5 rows
print(laps.head())

#checking size of the dataset
print("Number of rows:", len(laps))
print("Number of columns:", len(laps.columns))

# display all column names
print(laps.columns.tolist())

#display information about each column
print(laps.info())

#finding laps with missing lap durations
missing_laps = laps[laps["lap_duration"].isna()]

print("\nLaps with missing lap durations:")
print(missing_laps[["driver_number", "lap_number", "lap_duration"]])

#load driver info
drivers = pd.read_csv("data/raw/drivers.csv")

#match missing laps with driver teams and names

missing_laps_named = missing_laps.merge(drivers[["driver_number", "full_name", "team_name"]], on="driver_number", how="left")

print("\nMissing laps with driver info:")
print(missing_laps_named[["driver_number", "full_name", "team_name", "lap_number", "lap_duration"]])

#loading race results 

results = pd.read_csv("data/raw/session_result.csv")
results = results.merge(
    drivers[["driver_number", "full_name"]], 
    on="driver_number", 
    how="left"
)

#check for drivers with missing lap times

dnf_results = results[results["driver_number"].isin(missing_laps["driver_number"])]

print("\n Race results for drivers with missing lap times:")
print(dnf_results[["driver_number", "full_name", "position", "dnf", "dns", "dsq"]])


#creating dataset containing laps with valid durations
valid_laps = laps.dropna(subset=["lap_duration"])

print("\nNumber of valid laps:", len(valid_laps))
print("Number of excluded laps:", len(laps) - len(valid_laps))

#summary statistics for valid lap times
print("\nLap time summary statistics:")
print(valid_laps["lap_duration"].describe())

#median is approx. 82.27 seconds, mean is much higher at 118.5 seconds
#maximum lap duration is 2,434 seconds, which could be associated with a red flag or other interruption

#find laps longer than 120 seconds
long_laps = valid_laps[valid_laps["lap_duration"] > 120]
print("\nNumber of laps longer than 120 seconds:", len(long_laps))

print(long_laps[["driver_number", "lap_number", "lap_duration", "is_pit_out_lap"]].sort_values(by="lap_duration", ascending=False).head(15))

#results align with red flag after collison on lap 46

valid_laps = valid_laps.copy()#identifying laps affected by the red flag
valid_laps["red_flag_lap"] = valid_laps["lap_number"].isin([45,46])

print("\nLaps affected by red flag:")
print(valid_laps["red_flag_lap"].value_counts())

non_red_flag_laps = valid_laps[valid_laps["red_flag_lap"] == False]

print("\nLap time statistics excluding red flag laps:")
print(non_red_flag_laps["lap_duration"].describe())

