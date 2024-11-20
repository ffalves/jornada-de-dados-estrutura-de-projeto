import os
import glob
import pandas as pd
import openpyxl
from typing import List
from app.config import DATA_INPUT_PATH

input_path = DATA_INPUT_PATH

def extract_from_excel(input_path: str) -> List[pd.DataFrame]:
    """
    Function to read files from path and return a list of dataframes
    args: input_path {str}: path to the input folder
    return: a list of dataframes
    """

    if not os.path.exists(input_path):
        print(f'Directory does not exist: {input_path}')
        return []
    
    all_files = glob.glob(os.path.join(input_path, "*.xlsx"))

    # Verifying files:
    if not all_files:
        print(f'No file found in {input_path}')
        return []
              
    dataframe_list = []
    for file in all_files:
        print(f'Reading file: {file}')
        dataframe_list.append(pd.read_excel(file))
    
    return dataframe_list

if __name__ == '__main__':
    dataframe_list = extract_from_excel(DATA_INPUT_PATH)
    print(f'Total files: {len(dataframe_list)}')
    for i, df in enumerate(dataframe_list):
        print(f'File {i+1}: { df.shape[0]} rows, {df.shape[1]}) columns')
# The code above reads all files from the input folder, which is the path variable, and returns a list of dataframes.