import os 
import sys 
import pickle 
from src.exception import CustomException
from sklearn.metrics import r2_score
from src.logger import logging
from sqlalchemy import create_engine
import pandas as pd
import mysql.connector as connection

def save_function(file_path,obj):
    dir_path=os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path,"wb") as file_obj:
        pickle.dump(obj, file_obj)


def model_performance(X_train, y_train, X_test, y_test, models): 
    try: 
        report = {}
        for i in range(len(models)): 
            model = list(models.values())[i]
# Train models
            model.fit(X_train, y_train)
# Test data
            y_test_pred = model.predict(X_test)
            #R2 Score 
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report

    except Exception as e: 
        raise CustomException(e,sys)
    

def load_obj(file_path):
    try: 
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        file_path = os.path.join(project_dir, 'pipeline', file_path)
        with open(file_path, 'rb') as file_obj: 
            return pickle.load(file_obj)
    except Exception as e: 
        logging.info("Error in load_object fuction in utils")
        raise CustomException(e,sys)
    
def fetch_data_from_mysql(host, username, password, database, table, output_folder='data'):
    conn = connection.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )

    query = f'SELECT * FROM {table}'
    df = pd.read_sql(query, conn)
    conn.close()
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_file = os.path.join(output_folder, f'{table}.csv')
    df.to_csv(output_file, index=False)

    print(f'Data fetched and saved to: {output_file}')


fetch_data_from_mysql(host='localhost', username='root', password='Sneha_9601', database='carproject', table='carproject')  

 