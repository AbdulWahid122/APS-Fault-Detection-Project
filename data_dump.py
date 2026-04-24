import pymongo
import pandas as pd
import json

uri="mongodb://abdulwahidshaikh688:Mango619@ac-psmix2m-shard-00-00.c08uesf.mongodb.net:27017,ac-psmix2m-shard-00-01.c08uesf.mongodb.net:27017,ac-psmix2m-shard-00-02.c08uesf.mongodb.net:27017/?ssl=true&replicaSet=atlas-8i7c6e-shard-0&authSource=admin"

client=pymongo.MongoClient(uri)

DATA_FILE_PATH=r"C:\datascience Files\mybuildprojectsfromscratch\aps fault detection project\aps_failure_training_set1.csv"
DATABASE_NAME="PROJECT"
COLLECTION_NAME="APS_FAULT_DETECTION_PROJECT"

db=client[DATABASE_NAME]
collection=db[COLLECTION_NAME]

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape} ")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())

    print(json_record[0])

    #insert converted json record to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    