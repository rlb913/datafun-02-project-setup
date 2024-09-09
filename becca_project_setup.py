''' This module provides functions for creating a series of project folders. '''

#####################################
# Import Modules at the Top
#####################################

# Import modules from standard library
import pathlib
import time

# Import local modules (if necessary)
# import utils_becca
import utils_becca


#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)



#####################################
# Define Function 1. Create folders for a range of years
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    for year in range(start_year, end_year + 1):
        folder_name = f"{year}"
        folder_path = data_path.joinpath(folder_name)
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")

  

#####################################
# Define Function 2. Create folders from a list of names
#####################################

def create_folders_from_list(folder_names: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders for a given list with options to lowercase and remove spaces.
    
    Arguments:
    folder_names -- A list of folder names.
    to_lowercase -- Optionally convert names to lowercase.
    remove_spaces -- Optionally remove spaces from folder names.
    '''
    print(f"FUNCTION CALLED: create_folders_from_list")
    
    for name in folder_names:
        if to_lowercase:
            name = name.lower()
        if remove_spaces:
            name = name.replace(' ', '-')
        folder_path = data_path.joinpath(name)
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")

#####################################
# Define Function 3. Create prefixed folders
#####################################

def create_prefixed_folders(folder_names: list, prefix: str) -> None:
    '''
    Create folders for a given list with a prefix.
    
    Arguments:
    folder_names -- A list of folder names.
    prefix -- The prefix to the folder names.
    '''
    print(f"FUNCTION CALLED: create_prefixed_folders")
    
    for name in folder_names:
        folder_name = f"{prefix}{name}"
        folder_path = data_path.joinpath(folder_name)
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")

#####################################
# Define Function 4. Create folders periodically
#####################################

def create_folders_periodically(duration_secs: int, number_of_folders: int) -> None:
    '''
    Create folders periodically.
    
    Arguments:
    duration_secs -- The number of seconds between folder creation.
    number_of_folders -- The total number of folders to create.
    '''
    print(f"FUNCTION CALLED: create_folders_periodically every {duration_secs} seconds")

    folder_count = 1
    
    while folder_count <= number_of_folders:
        folder_name = f"folder-{folder_count}"
        folder_path = data_path.joinpath(folder_name)
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {folder_path}")
        folder_count += 1
        time.sleep(duration_secs)
        


#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module (commented out if utils_becca is not available)
    # print(f"Byline: {utils_becca.get_byline()}")
    print(f"Byline: {utils_becca.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs, number_of_folders=3)

    # Add options to force lowercase and remove spaces
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

