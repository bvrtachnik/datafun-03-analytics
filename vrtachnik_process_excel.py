"""
This script reads the world_population.xlsx file, 
extracts the top 3 most populated countries, 
and saves the result to a text file in data_processed.
"""

#####################################
# Import Modules
#####################################

import pathlib
import openpyxl  # Ensure we can process Excel files properly

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "data"
processed_folder_name = "data_processed"
excel_file = "world_population.xlsx"
output_filename = "top_3_worldpop.txt"

#####################################
# Define Functions
#####################################

def get_top_3_population(file_path: pathlib.Path):
    """
    Extracts the top 3 most populated countries from the Excel file.

    Args:
        file_path (pathlib.Path): Path to the Excel file.

    Returns:
        list: List of tuples (Country Name, Population)
    """
    try:
        workbook = openpyxl.load_workbook(file_path, read_only=True, data_only=True)
        sheet = workbook.active

        population_data = []  # List to store (Country, Population)

        for row_num, row in enumerate(sheet.iter_rows(min_row=6, max_row=222, values_only=True), start=6):
            if row is None or len(row) < 5:
                continue  # Skip empty or malformed rows

            country = row[3]  # Country name (Column D)
            population = row[4]  # Population (Column E)

            if country and population is not None:
                try:
                    population_str = str(population).replace(",", "").strip()
                    population_int = int(float(population_str))  # Convert to int
                    population_data.append((country, population_int))
                except (ValueError, TypeError):
                    continue  # Skip invalid rows

        # Sort by population in descending order and get the top 3
        top_3 = sorted(population_data, key=lambda x: x[1], reverse=True)[:3]
        return top_3

    except FileNotFoundError:
        print(f"Error: Excel file not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error processing Excel file: {e}")
        return None

def save_top_3_population():
    """
    Reads the Excel file, extracts the top 3 most populated countries, 
    and saves the data to a text file in data_processed.
    """
    input_file = pathlib.Path(fetched_folder_name) / excel_file  # Path to Excel file
    output_file = pathlib.Path(processed_folder_name) / output_filename  # Output path

    top_3 = get_top_3_population(input_file)

    if top_3:
        output_file.parent.mkdir(parents=True, exist_ok=True)  # Ensure folder exists
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write("Top 3 Most Populated Countries (2022):\n")
            outfile.write("=" * 50 + "\n")
            for country, population in top_3:
                outfile.write(f"{country}: {population:,} (thousands)\n")

        print(f"SUCCESS: Top 3 world populations saved to {output_file}")
    else:
        print("No valid data found in the Excel file.")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    save_top_3_population()
