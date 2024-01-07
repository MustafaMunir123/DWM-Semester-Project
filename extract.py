import pandas as pd
from sqlalchemy import create_engine

def extract_txt(path):
    text_file_path = f'{path}'
    df = pd.read_csv(text_file_path, sep='\t')
    return df

def extract_csv(path):
    df = pd.read_csv(f"{path}")
    return df


def extract_table(path):
    db_path = f'{path}'
    engine = create_engine(f'sqlite:///{db_path}')

    table_name = 'db_locations'
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql_query(query, engine)
    return df
    
