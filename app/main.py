import os # working with files and folders
import glob # list files
import pandas as pd
from typing import List
import openpyxl


path = 'data/input'

"""
Function to read files from data/input

args: input_path {str}: path to the input folder

return: a list of dataframes
"""

def extract_from_excel(input_path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(input_path, "*.xlsx"))

    # Verifying files
    if not all_files:
        print(f'No files found in {input_path}')
        return []

    dataframe_list = []
    for file in all_files:
        print(f'Reading file {file}')
        dataframe_list.append(pd.read_excel(file))
    
    return dataframe_list

if __name__ == "__main__":
    dataframe_list = extract_from_excel(path)
    print(f'Total files: {len(dataframe_list)}')
    for i, df in enumerate(dataframe_list):
        print(f'File {i+1}: {df.shape[0]} rows, {df.shape[1]} colums')
        
