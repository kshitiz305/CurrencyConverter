import csv
import requests
import pandas as pd
import yaml
import os, logging as log


def get_files_list(directory_name, allowed_formats=".csv"):
    """Get files from the directory.
    :param directory_name: The name of the directory to fetch files from
    :param allowed_formats: filter of files to be parsed
    :return: list of files
    """
    return " ".join([files for files in os.listdir(directory_name) if files.endswith(allowed_formats)])


def csvtodatafarame(filename) -> pd.DataFrame:
    """
    converts csv to datafranme
    :return: Dataframe for the csv
    :param: filename : file to be return as dataframe
    """
    df = pd.read_csv(filename, sep=get_delimiter(filename))
    return df


def storetodb(transaction):
    """
    stores the records in the database
    :param transaction:
    """
    pass


def cleaner(string):
    """
    string to be formate the string
    :param string:
    :return: string stripped of all whitespaces
    """
    if isinstance(string, (int, float)):
        return string
    return string.strip()


def get_delimiter(file_path, bytes=4096):
    """
    get the delimiter used in the csv file
    :param: file_path
    :return: delimited used
    """
    sniffer = csv.Sniffer()
    data = open(file_path, "r").read(bytes)
    delimiter = sniffer.sniff(data).delimiter
    return delimiter


def get_credentials():
    """
    Gets credential for the api key stored in the credential.yml
    """
    with open('credentials.yaml') as f:
        content = f.read()
    my_credentials = yaml.load(content, Loader=yaml.FullLoader)
    apikey = my_credentials['apikey']
    return apikey


def currency_converter(row):
    """
    Generates the amount in the row
    :param: Row for the csv
    :return: Returns the amount of the currency converted
    """
    row = [cleaner(i) for i in row]
    url = f"https://api.apilayer.com/fixer/convert?to={row[1]}&from={row[2]}&amount={row[3]}"
    apikey = get_credentials()
    payload = {}
    headers = {
        "apikey": apikey
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    json = response.json()

    if status_code == 200:
        return json.get("result")
    else:
        return "Invalid request"

def main():

    directory_name = input("Type folder name having files for transaction")
    # directory_name = 'CurrencyFolder'
    print("Files in the above mentioned forlder are: ", get_files_list(directory_name))
    file_name = input("Type file name to be progcessed")
    # file_name = "format1.csv"
    full_path = os.path.join(directory_name, file_name)
    log.info(f"Processing file {full_path}")
    df = csvtodatafarame(full_path)
    api_key = get_credentials()
    df["ConvertedAmount"] = df.apply(currency_converter, axis=1)

    # destination_path = "FINAL"
    destination_path = input("Type folder name to store the output")
    df.to_csv(os.path.join(destination_path, file_name))



if __name__ == "__main__":
    main()