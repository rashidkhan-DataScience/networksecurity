import os
import sys
import certifi
import pandas as pd
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')


class NetworkDataExtract:

    def __init__(self, database,collection):
        try:
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL,tlsCAFile=certifi.where())
            self.database = self.mongo_client[database]
            self.collection = self.database[collection]

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            records = data.to_dict(orient='records')
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_to_mongodb(self, records):
        try:
            self.collection.insert_many(records)
            return len(records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":

    file_path = r"D:\Projects\NetworkSecurity\Network_Data\phisingData.csv"

    network_data_extract = NetworkDataExtract('NetworSecurity','NetworkData')

    records = network_data_extract.csv_to_json_convertor(file_path)

    logging.info(f"Number of records extracted: {len(records)}")

    no_of_records = network_data_extract.insert_data_to_mongodb(records)

    print(f"Successfully inserted {no_of_records} records")