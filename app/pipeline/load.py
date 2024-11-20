import os
import pandas as pd
from app.config import DATA_OUTPUT_PATH


output_path = DATA_OUTPUT_PATH

def save_xlsx(dataframe: pd.DataFrame, output_path: str, filename: str):

    """
    Saves a DataFrame to an Excel file.

    Args:
        dataframe (pd.DataFrame): The DataFrame to save.
        output_path (str): The directory where the file will be saved.
        filename (str): The name of the Excel file.

    Returns:
        str: Message indicating the success or failure of the operation.
    """
    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError('dataframe must be a pandas DataFrame')
    
    if not isinstance(output_path, str):
        raise ValueError('output_path must be a string')
    
    if not isinstance(filename, str):
        raise ValueError('filename must be a string')
    
    if not os.path.exists(output_path):
        try:
            os.makedirs(output_path)
        except Exception as e:
            raise RuntimeError(f'Failed to create output directory: {output_path}')
    
    file_path = os.path.join(output_path, filename)
    try:
        dataframe.to_excel(file_path, index=False)

    except Exception as e:
        raise RuntimeError(f'Failed to save file at {file_path}. Error: {str(e)}')
    
    return f'File saved successfully at {output_path}/{filename}'




