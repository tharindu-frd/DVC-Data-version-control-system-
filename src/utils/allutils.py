import yaml
import os
import json


######## Lets create a function to read yaml files and return a dictionary
def read_yaml(path_to_yaml:str) -> dict:
       with open(path_to_yaml) as yaml_file:
              content = yaml.safe_load(yaml_file)
              return content



######## Lets create a function to create a directory
def create_directory(dirs:list):
       for dir_path in dirs:
              os.makedirs(dir_path,exist_ok=True)


###### Lets create a function to save a df in a given directory
def save_local_df(data,data_path,index_status=False):
       data.to_csv(data_path,index=index_status)



def save_reports(report: dict, report_path: str, indentation=4):
    with open(report_path, "w") as f:
        json.dump(report, f, indent=indentation)
    print(f"reports are saved at {report_path}")
