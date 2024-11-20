from app.pipeline.extract import extract_from_excel
from app.pipeline.transform import concatenate_dataframes
from app.pipeline.load import save_xlsx
from app.config import DATA_INPUT_PATH, DATA_OUTPUT_PATH
import datetime

if __name__ == '__main__':
    # Extract
    df_list = extract_from_excel(input_path = DATA_INPUT_PATH)
    # Transform
    df = concatenate_dataframes(df_list)
    # Create filename with datetime
    filename = f'output_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.xlsx'
    # Load
    save_xlsx(df, output_path = DATA_OUTPUT_PATH, filename=filename)