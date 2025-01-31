# datafun-03-analytics  
Repository for **Module 3 of Data Analytics Fundamentals** at **Northwest Missouri State University**  


## Overview
This project demonstrates how to fetch and process various types of 
data (Excel, JSON, text, and CSV) using Python. 

The repository includes:

- Four example fetchers: Scripts to retrieve data from the web.
- Four example processors: Scripts to analyze and process the fetched data.
- Four fetchers with scripts to retrieve data from the web
- Four processors with scripts to analyze and process fetched data

---

## Create and Activate Project Virtual Environment  

For Windows, navigate to the **local project folder** and create a virtual environment in the `.venv` folder.  

```shell
# Create virtual environment and virtual environment folder
py -m venv .venv

# Activate the virtual environment
.venv\Scripts\Activate

# Upgrade Pip and install dependencies
py -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt
```

## Fetchers

vrtachnik_get_csv.py 
   - Fetches a CSV file with global Covid 19 data
     
vrtachnik_get_excel.py
   - Fetches an excel file with the world's population ranked from highest to lowest
     
vrtachnik_get_json.py
   - Fetches a json file with the English Premier League Table results from the 1992/93 season to the 2018/19 season
     
vrtachnik_get_text.py
   - Fetches a text file with the content of *Moby Dick* by Herman Melville.

## Processors

vrtachnik_process_csv.py
   - Processor that processes the global Covid 19 data and lists the total cases and total cases per million per continent

vrtachnik_process_excel.py
   - Processor that processes the world population excel file and returns the 3 highest world populations

vrtachnik_process_json.py
   - Processor that processes the English Premier League results json file and returns the final annual season results for Manchester United from 1992/93 to 2018/19

vrtachnik_process_text.py
   - Processor that processes the Moby Dick text file and returns the count of times 'Ahab' is mentioned in the text

## Execution Commands

### Fetchers

```shell
py vrtachnik_get_csv.py
py vrtachnik_get_excel.py
py vrtachnik_get_json.py
py vrtachnik_get_text.py
```

### Processors

```shell
py vrtachnik_process_csv.py
py vrtachnik_process_excel.py
py vrtachnik_process_json.py
py vrtachnik_process_text.py
```

## Git Add-Commit-Push Workflow  

Use the following commands to track, commit, and push changes to the remote repository.  

```shell
# Step 1: Add all changes in your working directory to the staging area
git add .

# Step 2: Commit the staged changes to your local Git repository 
# -m allows you to include a commit message describing your changes
git commit -m "Your commit message here"

# Step 3: Push the local commits to the remote repository on GitHub
git push origin main

# (Only for first-time push) If this is your first push to a new repository:
git push -u origin main  # Sets upstream branch for future pushes
```
