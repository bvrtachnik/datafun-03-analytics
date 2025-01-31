"""
This file fetches an Excel file from the web, 
saves it to a local file named world_population.xlsx in a folder named data,
and ensures it is saved in a standard .xlsx format for easy processing.
"""

#####################################
# Import Modules at the Top
#####################################

# Import from Python Standard Library
import pathlib

# Import from external packages
import requests
import openpyxl  # Ensure we can process Excel files properly

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "data"
cleaned_excel_file = "world_population.xlsx"

#####################################
# Define Functions
#####################################

def fetch_excel_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch Excel data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the Excel file to fetch.

    Returns:
        None
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching Excel data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        raw_file = write_excel_file(folder_name, filename, response.content)
        
        # Convert to standard .xlsx format to ensure it's readable
        clean_excel_file(raw_file)
        
        logger.info(f"SUCCESS: Excel file fetched, cleaned, and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_excel_file(folder_name: str, filename: str, binary_data: bytes) -> pathlib.Path:
    """
    Write Excel binary data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        binary_data (bytes): Binary content of the Excel file.

    Returns:
        pathlib.Path: Path to the saved file.
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing Excel data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('wb') as file:
            file.write(binary_data)
        logger.info(f"SUCCESS: Excel data written to {file_path}")
        return file_path
    except IOError as io_err:
        logger.error(f"Error writing Excel data to {file_path}: {io_err}")
        return None

def clean_excel_file(file_path: pathlib.Path):
    """
    Open the downloaded Excel file and save it again in a standard .xlsx format.

    Args:
        file_path (pathlib.Path): Path to the downloaded Excel file.

    Returns:
        None
    """
    try:
        workbook = openpyxl.load_workbook(file_path)
        cleaned_path = file_path.parent / cleaned_excel_file
        workbook.save(cleaned_path)  # Save in a cleaned format
        logger.info(f"SUCCESS: Cleaned Excel file saved as {cleaned_path}")
    except Exception as e:
        logger.error(f"Error cleaning Excel file: {e}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching and cleaning Excel data.
    """
    excel_url = 'https://databank.worldbank.org/data/download/POP.xlsx'
    logger.info("Starting Excel fetch demonstration...")
    fetch_excel_file(fetched_folder_name, cleaned_excel_file, excel_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

# TODO: Run this script to ensure all functions work as intended.
