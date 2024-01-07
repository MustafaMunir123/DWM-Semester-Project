
# import pandas as pd
# from sqlalchemy import create_engine

"""
Table to csv
"""
# # Connect to the SQLite database
# db_path = 'db.sqlite3'
# engine = create_engine(f'sqlite:///{db_path}')

# # Read the table into a pandas DataFrame
# table_name = 'db_stock'
# query = f'SELECT * FROM {table_name}'
# df = pd.read_sql_query(query, engine)

# # Save the DataFrame to a CSV file
# csv_file_path = 'store.csv'
# df.to_csv(csv_file_path, index=False)


"""
    Text file to csv
"""
# import pandas as pd

# # Specify the path to your text file
# text_file_path = 'path/to/your/file.txt'

# # Use pandas to read the text file into a dataframe
# # You may need to adjust the delimiter or separator based on your file's format
# df = pd.read_csv(text_file_path, sep='\t')

# # Display the dataframe
# print(df)


"""
Drop Table 
"""
# from sqlalchemy import create_engine, MetaData

# database_url = 'sqlite:///locations.sqlite3'
# engine = create_engine(database_url, echo=False)

# metadata = MetaData()
# metadata.reflect(bind=engine)
# table_name_to_drop = 'db_store'

# if table_name_to_drop in metadata.tables:
#     table_to_drop = metadata.tables[table_name_to_drop]
#     table_to_drop.drop(engine)

#     print(f"Table '{table_name_to_drop}' has been dropped.")
# else:
#     print(f"Table '{table_name_to_drop}' does not exist.")

"""
db table to \t .txt
"""
import csv
from sqlalchemy import create_engine, select, MetaData

database_url = 'sqlite:///db.sqlite3'
engine = create_engine(database_url, echo=False)

metadata = MetaData()
metadata.reflect(bind=engine)
table_name_to_export = 'db_store'
if table_name_to_export in metadata.tables:
    table_to_export = metadata.tables[table_name_to_export]
    with engine.connect() as connection:
        select_statement = select(table_to_export)
        result = connection.execute(select_statement)
        column_names = result.keys()
        output_file_name = f'{table_name_to_export}_export.txt'
        with open(output_file_name, 'w', newline='') as output_file:
            csv_writer = csv.writer(output_file, delimiter='\t')
            csv_writer.writerow(column_names)
            csv_writer.writerows(result)

        print(f"Table '{table_name_to_export}' data has been exported to {output_file_name}.")
else:
    print(f"Table '{table_name_to_export}' does not exist.")


"""
Txt read
"""
import csv

# Replace 'YourTableName_export.txt' with the actual file name
input_file_name = 'db_store_export.txt'

# Open the file in read mode
with open(input_file_name, 'r', newline='') as input_file:
    # Create a CSV reader with tab as the delimiter
    csv_reader = csv.reader(input_file, delimiter='\t')

    # Read the header (column names)
    header = next(csv_reader)

    # Print the header
    print("Column Names:")
    print(header)

    # Read and print the data rows
    print("\nData Rows:")
    for row in csv_reader:
        print(row)
