import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('race_result.db')

# SQL query to extract the data
query = """
SELECT location, grid, position, fastest_lap, points, driver_name, race_name, time, year, team_name, date
FROM race_results
WHERE year = 2020
ORDER BY date;
"""

# Execute the query and load the data into a pandas DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

print(df)