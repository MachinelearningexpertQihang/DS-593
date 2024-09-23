
conn = sqlite3.connect('health_events_data.db')
df = pd.read_sql_query("SELECT * FROM health_events", conn)

# Fill missing numerical values with the mean
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Fill missing categorical values with the mode
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize text formatting (strip spaces and capitalize)
for col in categorical_cols:
    df[col] = df[col].str.strip().str.capitalize()
df.to_sql('cleaned_data', conn, if_exists='replace', index=False)

# Commit and close the connection
conn.commit()
conn.close()

print("Data cleaned and saved successfully in the 'cleaned_data' table!")