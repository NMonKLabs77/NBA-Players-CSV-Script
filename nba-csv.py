# Use API to extract information about nba players and store the results in a csv file called nba_players.csv

# Import all the modules needed for the script
# The python requests module is used for making http requests
# The CSV module provides functionality to both read from and write to CSV files
import requests
import csv
api_url = "https://free-nba.p.rapidapi.com/players" # Stored the URL endpoint in the variable api_url
querystring = {"page":"0","per_page":"25"} 

# Defined headers,parameters and the api_url
headers = {
	"X-RapidAPI-Key": "a84fdf16f3mshff2b50524d4c76ap1eac6cjsnd4c443486ec6",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

# Sent a GET request to the API using the url endpoint stored in the variable api_url
response = requests.get(api_url, headers=headers, params=querystring)

# Check if the request was successful
if response.status_code == 200:
    player_data = response.json()["data"]  # Converted the response to JSON and got the data key
else:
    print("Failed to retrieve data from the API.")
    exit()

# Defined the CSV file name
csv_filename = "nba_players.csv"

# Defined the headers for the CSV file
csv_headers = ["Player ID", "First Name", "Last Name", "Position", "Full Team Name"]

# Open the CSV file in write mode and formatted to new line with every column name surrounded by '' appearing on a new line
with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_headers)  # Write the headers to the CSV file

    # Iterate through the player data and extract relevant information
    for player in player_data:
        player_id = player["id"]
        first_name = player["first_name"]
        last_name = player["last_name"]
        position = player["position"]
        team = player["team"]["full_name"]

        # Write the player data to the CSV file
        writer.writerow([player_id, first_name, last_name, position, team])

# After the script is done, a message is printed to the screen telling me that the csv file has been created
print(f"CSV file '{csv_filename}' has been created.")

