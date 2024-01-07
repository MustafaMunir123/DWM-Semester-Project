from extract import (
    extract_csv,
    extract_table,
    extract_txt
)
from transform import (
    create_table_from_df
)
from load import (
    fact_table,
    dimension_table
)

print("\n\tEXTRACTING DATA FROM DIFFERENT SOURCES\n")

locations_df = extract_table(path="data/locations.sqlite3")
store_df = extract_txt(path="data/store.txt")
stock_df = extract_csv(path="data/stock.csv")

print("\n\tTRANSFORMING DATA INTO RDBMS\n")

create_table_from_df(stock_df, 'stock')
create_table_from_df(store_df, 'store')
create_table_from_df(locations_df, 'location')

print("\n\tLOADING DATA INTO STAR SCHEMA A MODEL OF DWH\n")

fact_table()
dimension_table()