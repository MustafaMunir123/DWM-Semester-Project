from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


def fact_table(db_path='merged_db.sqlite3'):
    engine = create_engine(f'sqlite:///{db_path}')
    query = text('CREATE TABLE IF NOT EXISTS FACT_STOCK AS SELECT \
        stock.price_purchased, stock.price_sold, store.location_id,\
            stock.store_id, stock.id  FROM stock, store')
    
    try:
        with engine.connect() as connection:
            connection.execute(query)
        print("Table 'FACT_STOCK' created successfully.")
    except SQLAlchemyError as e:
        print(f"Error creating table: {e}")


def dimension_table(db_path='merged_db.sqlite3'):
    engine = create_engine(f'sqlite:///{db_path}')
    query = text('CREATE TABLE IF NOT EXISTS DIM_STOCK AS \
        SELECT stock.date_purchased, stock.date_sold,\
            stock.name, stock.id  FROM stock')
    
    try:
        with engine.connect() as connection:
            connection.execute(query)
        print("Table 'FACT_STOCK' created successfully.")
    except SQLAlchemyError as e:
        print(f"Error creating table: {e}")
        
        
    query = text('CREATE TABLE IF NOT EXISTS DIM_STORE AS SELECT * FROM store')
    
    try:
        with engine.connect() as connection:
            connection.execute(query)
        print("Table 'DIM_STORE' created successfully.")
    except SQLAlchemyError as e:
        print(f"Error creating table: {e}")
        
    
    query = text('CREATE TABLE IF NOT EXISTS DIM_LOCATION AS SELECT * FROM location')
    
    try:
        with engine.connect() as connection:
            connection.execute(query)
        print("Table 'FACT_STOCK' created successfully.")
    except SQLAlchemyError as e:
        print(f"Error creating table: {e}")
        
    
# dimension_table()