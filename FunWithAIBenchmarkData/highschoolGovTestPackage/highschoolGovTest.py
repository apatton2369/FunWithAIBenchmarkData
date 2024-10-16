#highschoolGovTest

import csv
def csvFile():
    csvData = [] ## Open the CSV file
    with open(".data/high_school_government_and_politics_test.csv", mode='r') as questionFile:
        reader =csv.reader(questionFile) # Read each row and append it to the csvData list
        for row in reader:
            csvData.append(row)
            return csvData
