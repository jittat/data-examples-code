import csv

csvfile = open('scores.csv')
reader = csv.DictReader(csvfile)
for row in reader:
    print(row)

csvfile.close()
