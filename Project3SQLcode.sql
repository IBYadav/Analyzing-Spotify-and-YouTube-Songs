
# -- Load the sql extention ----
%load_ext sql
# --- Load your mysql db using credentials from the "DB" area ---
%sql mysql+pymysql://b3fa8e1a:Cab#22se@localhost/b3fa8e1a

%%sql
SELECT Track, Views
FROM cleaned_dataset
ORDER BY Views DESC
LIMIT 1;

%%sql
SELECT Track,Stream
FROM cleaned_dataset
ORDER BY Stream DESC
LIMIT 1;

%%sql
SELECT Track,EnergyLiveness
FROM cleaned_dataset
ORDER BY EnergyLiveness DESC
LIMIT 5;

%%sql
SELECT COUNT(*) AS Track, most_playedon
FROM cleaned_dataset
WHERE artist = 'Black Eyed Peas'
GROUP BY most_playedon;

%%sql
SELECT Track, Likes, Energy,Tempo
FROM cleaned_dataset
WHERE artist = 'Gorillaz'
ORDER BY Likes DESC
LIMIT 1;

%%sql
SELECT Album_type, COUNT(*) AS COUNT_Album_type
FROM cleaned_dataset
GROUP BY Album_type;

%%sql
SELECT Track,
SUM(Views + Stream) AS Total_Count
FROM cleaned_dataset
GROUP BY Track
ORDER BY Total_Count DESC
LIMIT 5;