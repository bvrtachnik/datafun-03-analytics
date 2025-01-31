"""
This script reads a JSON file containing Premier League season tables,
filters the performance of Manchester United in each season,
and saves the results to a text file in the 'data_processed' folder.
"""

#####################################
# Import Modules
#####################################

import pathlib
import json

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "data"
processed_folder_name = "data_processed"
json_file_name = "premier_league_table.json"  # ✅ Updated file name
output_filename = "manchester_united_table.txt"
team_name = "Manchester United"

#####################################
# Define Functions
#####################################

def get_manchester_united_table(file_path: pathlib.Path):
    """
    Reads the JSON file and extracts Manchester United's performance each season.

    Args:
        file_path (pathlib.Path): Path to the JSON file.

    Returns:
        list: List of season records for Manchester United.
    """
    try:
        with file_path.open('r', encoding="utf-8") as file:
            league_data = json.load(file)

        # Ensure the file contains season data
        united_performance = []

        for season in league_data:  # Loop through each season
            season_year = season.get("season", "Unknown Season")
            table = season.get("table", [])

            for team_data in table:  # Loop through each team's data
                if team_data.get("team", "") == team_name:
                    record = (
                        f"Season: {season_year}\n"
                        f"Position: {team_data.get('position', 'N/A')}\n"
                        f"Played: {team_data.get('played', 'N/A')}\n"
                        f"Points: {team_data.get('points', 'N/A')}\n"
                        f"Goal Difference: {team_data.get('goal_difference', 'N/A')}\n"
                        f"Won: {team_data.get('won', 'N/A')}\n"
                        f"Draw: {team_data.get('draw', 'N/A')}\n"
                        f"Loss: {team_data.get('loss', 'N/A')}\n"
                        f"Goals Scored: {team_data.get('goals_scored', 'N/A')}\n"
                        f"Goals Against: {team_data.get('goals_against', 'N/A')}\n"
                        "==================================================\n"
                    )
                    united_performance.append(record)

        return united_performance

    except FileNotFoundError:
        print(f"Error: JSON file not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return None
    except Exception as e:
        print(f"Error processing JSON file: {e}")
        return None

def save_manchester_united_table():
    """
    Reads the JSON file, extracts Manchester United's performance, 
    and saves it to a text file in the 'data_processed' folder.
    """
    input_file = pathlib.Path(fetched_folder_name) / json_file_name
    output_file = pathlib.Path(processed_folder_name) / output_filename

    united_performance = get_manchester_united_table(input_file)

    if united_performance:
        output_file.parent.mkdir(parents=True, exist_ok=True)  # Ensure folder exists
        with output_file.open('w', encoding="utf-8") as outfile:
            outfile.write("Manchester United Season Performance:\n")
            outfile.write("=" * 50 + "\n")
            for record in united_performance:
                outfile.write(record + "\n")

        print(f"SUCCESS: Manchester United season table saved to {output_file}")
    else:
        print("No valid data found in the JSON file.")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    save_manchester_united_table()
