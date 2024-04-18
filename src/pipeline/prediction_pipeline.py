import sys
import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_obj

class PredictPipeline:
    def __init__(self)->None:
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor= load_obj(preprocessor_path)
            model=load_obj(model_path)

            data_scaled=preprocessor.transform(features)
            pred=model.predict(data_scaled)
            return pred
        except Exception as e:
            logging.info("Error occured in predict function in prediction_pipeline location")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self, Year:int, 
                     Owner:int,
                     Present_Price:float, 
                     Kms_Driven:int, 
                     Fuel_Type:str, 
                     Seller_Type:str, 
                     Transmission:str):
     self.Year = Year
     self.Owner = Owner
     self.Present_Price = Present_Price
     self.Kms_Driven = Kms_Driven
     self.Fuel_Type = Fuel_Type
     self.Seller_Type = Seller_Type
     self.Transmission= Transmission	 
        
    def get_data_as_dataframe(self): 
             try: 
                  custom_data_input_dict = {
                       'Year': [self.Year], 
                       'Owner': [self.Owner],
                       'Present_Price': [self.Present_Price],
                       'Kms_Driven': [self.Kms_Driven], 
                       'Fuel_Type': [self.Fuel_Type], 
                       'Seller_Type':[self.Seller_Type],
                       'Transmission': [self.Transmission] 

                  }
                  df = pd.DataFrame(custom_data_input_dict)
                  logging.info(f"Dataframe created : {df}")
                  return df
             except Exception as e:
                  logging.info("Error occured in get_data_as_dataframe function in prediction_pipeline")
                  raise CustomException(e,sys) 