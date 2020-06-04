import sys
import csv
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
def portfolio_cost(filename):
    result = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        _ = next(rows)
        for line in f:
            try:
                row = line.split(',')
                summ = float(row[1]) * float(row[2])
                result += summ
            except ValueError:
                print('Shit happens')
    return result
cost = portfolio_cost(filename)
print('Total cost:', cost)