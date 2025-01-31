"""
Process an Excel file to filter the top 25 countries by population and save the results as a text file.
"""

#####################################
# Import Modules
#####################################

import pathlib
import openpyxl

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

def get_top_25_countries(file_path: pathlib.Path) -> list:
    """
    Extracts the top 25 countries with the highest population from the Excel file.

    Args:
        file_path (pathlib.Path): Path to the Excel file.

    Returns:
        list: A list of tuples containing country names and formatted populations.
    """
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        country_population = []

        # Loop through the data rows, skipping the first few header rows
        for row in sheet.iter_rows(min_row=5, max_row=30, values_only=True):  
            country = row[2]  # Column C - Country Name
            population = row[4]  # Column E - Population

            if country and population:
                # Ensure population is a number before formatting
                try:
                    formatted_population = f"{int(str(population).replace(',', '')):,}"
                    country_population.append((country, formatted_population))
                except ValueError:
                    logger.warning(f"Skipping invalid population value: {population}")

        # Sort by population in descending order
        country_population.sort(key=lambda x: int(x[1].replace(',', '')), reverse=True)

        # Return only the top 25
        return country_population[:25]

    except Exception as e:
        logger.error(f"Error processing Excel file: {e}")
        return []

def process_excel_file():
    """
    Read an Excel file, extract the top 25 countries by population, and save results as a text file.
    """
    input_file = pathlib.Path(fetched_folder_name, "population_data.xlsx")
    output_file = pathlib.Path(processed_folder_name, "top_25_countries_by_population.txt")

    top_countries = get_top_25_countries(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Save results to a plain text file
    with output_file.open('w', encoding='utf-8') as file:
        file.write("Top 25 Countries by Population (2022):\n")
        file.write("=" * 40 + "\n")

        for country, population in top_countries:
            file.write(f"{country}: {population}\n")

    logger.info(f"Processed Excel file: {input_file}, Data saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")