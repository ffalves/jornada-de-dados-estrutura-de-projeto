import pandas as pd
from typing import List

def concatenate_dataframes(dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
        Concatenates a list of pandas DataFrames into a single DataFrame.

        Args:
            dataframe_list (List[pd.DataFrame]): A list of pandas DataFrames to concatenate.

        Returns:
            pd.DataFrame: A single concatenated DataFrame.

        Raises:
            ValueError: If the input list is empty or contains non-DataFrame elements.
    """
    if not dataframe_list:
        raise ValueError("Input list is empty.")
    
    if not all(isinstance(df, pd.DataFrame) for df in dataframe_list):
        raise ValueError("Input list contains non-DataFrame elements.")
    
    try:
        result = pd.concat(dataframe_list, ignore_index=True)
    except ValueError as e:
        raise RuntimeError(f'Failed to concatenate DataFrames: {e}')
    
    return result