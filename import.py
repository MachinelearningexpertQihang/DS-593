import sqlite3
import pandas as pd

# Path to the CSV file
csv_file = '/mnt/data/funny_epidemiological_events.csv'

# Load CSV into a DataFrame
df = pd.read_csv(csv_file)

conn = sqlite3.connect('health_events_data.db')

# Save the DataFrame to the SQLite table
df.to_sql('health_events', conn, if_exists='replace', index=False)

# Commit and close the connection
conn.commit()
conn.close()

print("Data imported successfully from funny_epidemiological_events.csv!")