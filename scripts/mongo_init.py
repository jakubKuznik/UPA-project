# UPA - project 1
# FIT BUT 2023/2024
# xsvobo1x, xkuzni04, xkanko00

import os

import requests
from pymongo import MongoClient
import json


def downloadAndSaveFile(url, targetFolder, fileName):
    try:
        # Download the file from the internet
        response = requests.get(url)
        response.raise_for_status()  # Check for download errors

        # Get the file name from the URL
        fileName = os.path.join(targetFolder, fileName)

        # Save the file to the specified folder
        with open(fileName, 'wb') as file:
            file.write(response.content)

        print(f'File has been downloaded and saved to {fileName}')
    except Exception as e:
        print(f'Error: {e}')


def load_json_to_dict(file_path):
    with open(file_path, 'r', encoding="utf8") as json_file:
        json_data = json.load(json_file)
    return json_data


def reformat_data_id(data, id_name):
    inserted_data = []
    for feature in data['features']:
        feature_properties = feature['properties']
        feature_properties['location'] = feature['geometry']
        _id = feature_properties.get(id_name)
        if _id:
            feature_properties['_id'] = _id
            inserted_data.append(feature_properties)

    return inserted_data


# Enter the file URL and target folder
targetFolder = os.path.dirname(os.path.abspath(__file__))
fileUrl1 = 'https://data.brno.cz/datasets/mestobrno::p%C3%ADtka-drinking-fountains.geojson?where=1=1&outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D'
fileName1 = "pitka.geojson"
fileUrl2 = "https://data.brno.cz/datasets/mestobrno::hranice-m%C4%9Bstsk%C3%BDch-%C4%8D%C3%A1st%C3%AD-city-districts-boundaries.geojson?where=1=1&outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D"
fileName2 = "hranice_casti.geojson"

# Call the function to download the file
downloadAndSaveFile(fileUrl1, targetFolder, fileName1)
downloadAndSaveFile(fileUrl2, targetFolder, fileName2)

# Zavolejte funkci pro načtení GeoJSON souboru
pitka_dict = load_json_to_dict(fileName1)
hranice_dict = load_json_to_dict(fileName2)

client = MongoClient("mongodb://username:password@address:port")

# Vyberte nebo vytvořte databázi
db = client.get_database("Brno_data")
db["pitka"].drop()
pitka_collection = db.create_collection("pitka")
db["hranice"].drop()
hranice_collection = db.create_collection("hranice")


data_to_upsert = load_json_to_dict("pitka_upsert.geojson")

# Získání vlastního "_id" z pole "OBJECTID" a vložení dat
data_to_insert = reformat_data_id(pitka_dict, 'OBJECTID')

if data_to_insert:
    pitka_collection.insert_many(data_to_insert)

data_to_upsert = reformat_data_id(data_to_upsert, "OBJECTID")

# Provedeni upsert do kolekce pitka
for one_value in data_to_upsert:
     pitka_collection.replace_one(filter={"_id": one_value["_id"]}, replacement=one_value, upsert=True)

# Získání vlastního "_id" z pole "OBJECTID" a vložení dat
data_to_insert = reformat_data_id(hranice_dict, 'ObjectId')

if data_to_insert:
    hranice_collection.insert_many(data_to_insert)

pitka_collection.create_index([("location", "2dsphere")])
hranice_collection.create_index([("location", "2dsphere")])

# Vyhledani vsech pitek v Brno-stred, ktere maji v nazvu slovo Park.
for pitka in pitka_collection.find({"TITLE": {"$regex": ".*Park.*", "$options": "i"}}):
    point = pitka.get('location')
    if point:
        # Najdi městskou část, do které pítko patří
        cast = hranice_collection.find_one({
            'location': {
                '$geoIntersects': {
                    '$geometry': point
                }
            },
            'nazev': 'Brno-střed'  # Předpokládám, že název městské části je uložen v poli 'name'
        })

        if cast:
            print(pitka)

client.close()
