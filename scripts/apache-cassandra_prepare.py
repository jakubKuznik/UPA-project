# UPA - project 1
# FIT BUT 2023/2024
# xsvobo1x, xkuzni04, xkanko00

# This script prepares an input CSV file for import into an Apache Cassandra database.
# It removes specified columns from the input CSV file, adds a UUID column at the beginning, and reformats a date column. 

import csv
import uuid
from datetime import datetime

# input and output files
input_csv_file = 'apache-cassandra_prepare-data.csv'
output_csv_file = 'data.csv'

# list of columns to remove
columns_to_remove = [
    'X', 'Y', 'objectid', 'join_count', 'target_fid',
    'id', 'd', 'e', 'den', 'rok',
    'mesic', 'mesic_t', 'den_v_tydnu', 'point_x', 'point_y', 'globalid'
]

# process the csv file
with open(input_csv_file, 'r', newline='', encoding='utf-8-sig') as csv_input, open(output_csv_file, 'w', newline='') as csv_output:
    csvreader = csv.reader(csv_input)
    csvwriter = csv.writer(csv_output)
    header = next(csvreader)

    # create a list of updated fieldnames (add uuid column to the beginning and remove columns)
    updated_fieldnames = ['uuid'] + [field for field in header if field not in columns_to_remove]

    # write the updated header
    csvwriter.writerow(updated_fieldnames)

    # add uuid to the each row and add the specified columns
    for row in csvreader:
        # include only the updated columns
        new_row = [row[i] for i, field in enumerate(header) if field not in columns_to_remove]

        # generate the UUID
        my_uuid = str(uuid.uuid4())
        new_row.insert(0, my_uuid)

        # transform the date format (date is in the first row)
        original_date = new_row[1]
        try:
            datetime_obj = datetime.strptime(original_date, "%Y/%m/%d %H:%M:%S+%f")
            formatted_date = datetime_obj.strftime("%Y-%m-%d")
            new_row[1] = formatted_date
        except ValueError: # in the case of failed transformation do not transform the date
            pass

        # add the updated row to the output CSV
        csvwriter.writerow(new_row)

