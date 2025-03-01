"""
Process a CSV file on COVID-19 data to calculate total cases and total cases per million by continent.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
from collections import defaultdict

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################

def analyze_covid_data(file_path: pathlib.Path) -> dict:
    """
    Analyze the COVID-19 dataset to calculate total cases and total cases per million by continent.

    Args:
        file_path (pathlib.Path): The path to the CSV file.

    Returns:
        dict: A dictionary with continent as keys and aggregated total cases & total cases per million.
    """
    try:
        # Initialize dictionaries to store summed data
        continent_cases = defaultdict(float)
        continent_cases_per_million = defaultdict(float)

        with file_path.open('r', encoding='utf-8') as file:
            dict_reader = csv.DictReader(file)
            for row in dict_reader:
                try:
                    continent = row["continent"].strip()
                    if not continent:  # Skip empty continent values
                        continue

                    # Extract values and convert to float (handle missing values)
                    total_cases = float(row["total_cases"]) if row["total_cases"] else 0
                    cases_per_million = float(row["total_cases_per_million"]) if row["total_cases_per_million"] else 0

                    # Aggregate data
                    continent_cases[continent] += total_cases
                    continent_cases_per_million[continent] += cases_per_million

                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")

        # Store results in a dictionary
        stats = {
            continent: {
                "total_cases": continent_cases[continent],
                "total_cases_per_million": continent_cases_per_million[continent]
            }
            for continent in continent_cases
        }
        return stats

    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """
    Read the COVID-19 CSV file, analyze total cases by continent, and save the results.
    """
    input_file = pathlib.Path(fetched_folder_name, "covid_19_data.csv")
    output_file = pathlib.Path(processed_folder_name, "covid_cases_by_continent.txt")

    stats = analyze_covid_data(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open('w', encoding='utf-8') as file:
        file.write("COVID-19 Total Cases by Continent:\n")
        for continent, values in stats.items():
            file.write(f"{continent}:\n")
            file.write(f"  Total Cases: {values['total_cases']:.0f}\n")
            file.write(f"  Total Cases per Million: {values['total_cases_per_million']:.2f}\n")
            file.write("\n")

    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting COVID-19 CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")
