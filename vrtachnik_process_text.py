"""
This script reads a text file containing the novel Moby Dick,
counts occurrences of the word "Ahab" (case-insensitive),
and saves the result to a text file in the 'data_processed' folder.
"""

#####################################
# Import Modules
#####################################

import pathlib

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "data"
processed_folder_name = "data_processed"
text_file_name = "moby_dick.txt"
output_filename = "ahab_name_count.txt"
word_to_count = "Ahab"

#####################################
# Define Functions
#####################################

def count_word_occurrences(file_path: pathlib.Path, word: str) -> int:
    """
    Count the occurrences of a specific word in a text file (case-insensitive).

    Args:
        file_path (pathlib.Path): Path to the text file.
        word (str): The word to count.

    Returns:
        int: Number of times the word appears.
    """
    try:
        with file_path.open('r', encoding="utf-8") as file:
            content = file.read()
            return content.lower().count(word.lower())
    except FileNotFoundError:
        print(f"Error: Text file not found at {file_path}")
        return 0
    except Exception as e:
        print(f"Error reading text file: {e}")
        return 0

def save_word_count():
    """
    Reads the text file, counts occurrences of "Ahab",
    and saves the result to a text file in 'data_processed'.
    """
    input_file = pathlib.Path(fetched_folder_name) / text_file_name
    output_file = pathlib.Path(processed_folder_name) / output_filename

    word_count = count_word_occurrences(input_file, word_to_count)

    output_file.parent.mkdir(parents=True, exist_ok=True)  # Ensure folder exists
    with output_file.open('w', encoding="utf-8") as outfile:
        outfile.write(f"Occurrences of '{word_to_count}': {word_count}\n")

    print(f"SUCCESS: Word count saved to {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    save_word_count()
