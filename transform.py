from sqlalchemy import create_engine

def create_table_from_df(df, table_name, db_path='merged_db.sqlite3'):
    engine = create_engine(f'sqlite:///{db_path}')
    df.to_sql(table_name, engine, index=False, if_exists='replace')

    print(f"Table '{table_name}' created from DataFrame.")

