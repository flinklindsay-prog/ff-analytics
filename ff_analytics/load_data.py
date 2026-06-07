import pandas as pd
import duckdb
import os

# Create data/raw directory if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Pull weekly player stats 2020-2024
print("Downloading weekly stats...")
weekly = pd.read_csv("https://github.com/nflverse/nflverse-data/releases/download/player_stats/player_stats.csv.gz", compression="gzip")
weekly.to_csv("data/raw/weekly_stats.csv", index=False)
print(f"Weekly stats: {len(weekly)} rows")

# Pull rosters/player metadata
print("Downloading rosters...")
rosters = pd.read_csv("https://github.com/nflverse/nflverse-data/releases/download/rosters/roster_2024.csv.gz", compression="gzip")
rosters.to_csv("data/raw/rosters.csv", index=False)
print(f"Rosters: {len(rosters)} rows")

print("Done! Check data/raw/")