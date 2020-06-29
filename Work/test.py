import csv
import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)        
        for rowno, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                portfolio.append(record)    
            except:
                print(f'Row {rowno}: Bad row: {row}')     
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

def make_report(portfolio, prices):
    rows = []
    for d in portfolio:
        cprice = prices[d['name']]
        change = cprice - float(d['price'])
        summary = (d['name'], int(d['shares']), cprice, change)
        rows.append(summary)
    return rows

portfolio = read_portfolio(filename)
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

tcost = 0.0
tvalue = 0.0
for i in portfolio:                          
    tcost += int(i['shares'])*float(i['price'])
for i in portfolio:                           
    tvalue += float(i['shares'])*prices[i['name']]

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
