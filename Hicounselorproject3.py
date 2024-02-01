#--- Import Pandas ---
import pandas as pd
#--- Read in dataset ----
#file_path = './Spotify_Youtube.csv'
file_path = 'C:/Users/User/Documents/DATAMINING6212/Spotify_Youtube.csv'

df = pd.read_csv(file_path)
# ---WRITE YOUR CODE FOR TASK 1 ---
df.drop(["Url_spotify","Uri", "Key", "Url_youtube","Description"], axis=1, inplace=True)

# --- WRITE YOUR CODE ...
df.isna()
null_values= df.isna().sum()
#--- Inspect data ---
null_values

# --- WRITE YOUR CODE FOR TASK 3 ---
# Assuming your DataFrame is named df
columns = ['Danceability', 'Energy', 'Loudness', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo', 'Views', 'Likes', 'Comments', 'Duration_ms', 'Stream']
columns1 = ['Title', 'Channel', 'Licensed', 'official_video']

# Fill missing values with 0 for specified columns
df.loc[:, columns] = df.loc[:, columns].fillna(0)

# Fill missing values with 'NA' for specified columns
df.loc[:, columns1] = df.loc[:, columns1].fillna('NA')

# Inspect the modified data
df

# --- WRITE YOUR CODE FOR TASK 4 ---
df.drop_duplicates(inplace=True, keep='first')
#--- Inspect data ---
df

# --- WRITE YOUR CODE FOR TASK 5 ---
df.Duration_ms
df['Duration_ms'] = df['Duration_ms']/60000
# Inspect the modified 'df' DataFrame
#--- Inspect data ---
df

# --- WRITE YOUR CODE FOR TASK 6 ---
df.rename(columns={'Duration_ms': 'Duration_min'}, inplace=True)
#--- Inspect data ---
df

# --- WRITE YOUR CODE FOR TASK 8 ---
df['EnergyLiveness'] = df['Energy']/df['Liveness']
#--- Inspect data ---
df

# --- WRITE YOUR CODE FOR TASK 9 ---
# Convert the 'Column_Name' to a different data type (e.g., int)
df['Views'] = df['Views'].astype('float64')

#--- Inspect data ---
df

# --- WRITE YOUR CODE FOR TASK 10 ---
df['most_playedon'] = 'Spotify'
df.loc[df['Views'] >= df['Stream'], 'most_playedon'] = 'Youtube'
df['most_playedon'] = df['most_playedon'].astype('object')
df['most_playedon'].replace({False: 'Spotify', True: 'Youtube'}, inplace=True)

# Inspect the 'most_playedon' column
df['most_playedon']


# ...WRITE YOUR CODE FOR TASK 11 ...
#export the cleaned data
df.to_csv('C:/Users/User/Documents/DATAMINING6212/cleaned_dataset.csv', index=False)
#--- Inspect data ---
df
