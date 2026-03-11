import os
import pandas as pd
import time
import logging
from sqlalchemy import create_engine

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, db_engine):
    '''this fun will ingest the dataframe into database table'''
    df.to_sql(table_name, db_engine,
              if_exists='append',
              index=False)
    print(f"Ingested {table_name} into database")

def load_raw_data():
    start = time.time()
    for file in os.listdir():
        if file.endswith('.csv'):
            logging.info(f'Ingesting {file} in db')
            ingest_db(file, file[:-4], engine)
    end = time.time()
    logging.info(f'Total Time Taken: {(end-start)/60} minutes')

if __name__ == '__main__':
    load_raw_data()