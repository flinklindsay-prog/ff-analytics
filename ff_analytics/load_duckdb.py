import duckdb
import pandas as pd

con = duckdb.connect("data/ff_analytics.duckdb")

# Load weekly stats
weekly = pd.read_csv("data/raw/weekly_stats.csv")
con.execute("CREATE OR REPLACE TABLE raw_weekly_stats AS SELECT * FROM weekly")
print("Loaded raw_weekly_stats:", con.execute("SELECT COUNT(*) FROM raw_weekly_stats").fetchone()[0], "rows")

# Load rosters
rosters = pd.read_csv("data/raw/rosters.csv")
con.execute("CREATE OR REPLACE TABLE raw_rosters AS SELECT * FROM rosters")
print("Loaded raw_rosters:", con.execute("SELECT COUNT(*) FROM raw_rosters").fetchone()[0], "rows")

con.close()
print("DuckDB database saved to data/ff_analytics.duckdb")  