"""
csv files stand for comma separated variables/values.
In this excercise we are using two csv files and merging them into csv file
The challenge in this type of excercise is even though there are two different kidn of data
available thre program should be able to recognise the data and avoid losing any data
"""

import csv

def merger_csv(list_of_files: list, output_file):
    # create a field name for both the file which is list
    field_names = list()
    for file in list_of_files:
        with open(file, 'r') as input_csv:
            temp_field_name = csv.DictReader(input_csv).fieldnames
            field_names.extend(x for x in temp_field_name if x not in field_names)

    # write the fields individually to the output file
    with open(output_file, 'w', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames= field_names)
        writer.writeheader()
        for file in list_of_files:
            with open(file, 'r') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)

if __name__ == '__main__':
    merger_csv(list_of_files=('SampleCSVFile_2kb.csv','SampleCSVFile_11kb.csv'),output_file='New_csv_file.csv')