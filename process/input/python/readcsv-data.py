import csv

def read_csv_data(filename):
    results = []
    csvfile = open(filename)
    reader = csv.DictReader(csvfile)
    for row in reader:
        results.append(row)
    csvfile.close()

    return results

data = read_csv_data('scores.csv')
for d in data:
    print(d['name'], d['score'])
