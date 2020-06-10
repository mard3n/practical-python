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
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:                
                nshares = int(record['shares'])
                price = float(record['price'])
                result += nshares * price
            except ValueError:
                print(f'Ro  w {rowno}: Bad row: {row}')
    return result
cost = portfolio_cost(filename)
print('Total cost:', cost)