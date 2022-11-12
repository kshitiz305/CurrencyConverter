import requests
import pandas as pd
import yaml
import os , logging as log


def get_files_list(directory_name, allowed_formats = ".csv"):
    return " ".join([files for files in os.listdir(directory_name) if files.endswith(allowed_formats)])


def csvtodatafarame(filename):
    df = pd.read_csv(filename)
    return df


def storetodb(transaction):
    pass

def cleaner(string):
    if isinstance(string,(int,float)):
        return string
    return string.strip()

def get_credentials():
    with open('credentials.yaml') as f:
        content = f.read()
    my_credentials = yaml.load(content, Loader=yaml.FullLoader)
    apikey = my_credentials['apikey']
    return apikey

def currency_converter(row):
    row = [cleaner(i) for i in row]
    url = f"https://api.apilayer.com/fixer/convert?to={row[1]}&from={row[2]}&amount={row[3]}"
    apikey = get_credentials()
    payload = {}
    headers = {
        "apikey":apikey
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    json = response.json()

    if status_code == 200:
        return json.get("result")
    else:
        return "Invalid request"





# directory_name = input("Type folder name having files for transaction")
directory_name = 'CurrencyFolder'
print("Files in the above mentioned forlder are: ",get_files_list(directory_name))
# file_name = input("Type file name to be prgocessed")
file_name = "format1.csv"

full_path = os.path.join(directory_name,file_name)
log.info(f"Processing file {full_path}")
df = csvtodatafarame(full_path)
api_key = get_credentials()
df["ConvertedAmount"] = df.apply(currency_converter,axis = 1)

destination_path = "FINAL"
print(df)

df.to_csv(os.path.join(destination_path,file_name))