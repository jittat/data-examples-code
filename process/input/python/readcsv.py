import csv

csvfile = open('scores.csv')
reader = csv.reader(csvfile)
for row in reader:
    print(row)

csvfile.close()
