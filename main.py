
from credit_card_faulty.pipeline.training_pipeline import start_training_pipeline
from credit_card_faulty.pipeline.batch_prediction import start_batch_prediction

file_path="C:\\Users\\prash\\Downloads\\creditcard\\credit_card\\creditcard.csv"
print(__name__)
if __name__=="__main__":
     try:
          #start_training_pipeline()
          output_file = start_batch_prediction(input_file_path=file_path)
          print(output_file)
     except Exception as e:
          print(e)