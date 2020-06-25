import csv
import sys
#if len(sys.argv) == 2:
#    filename = sys.argv[1]
#else: 
#    filename = 'Data/portfolio.csv'

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)        
        select = ['name', 'shares', 'price']
        indices = [ headers.index(colname) for colname in select ]        
        portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
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

def print_report(reportdata):
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfoliofile,pricefile): 
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    report = make_report(portfolio,prices)
    print_report(report)
portfolio_report('Data/portfolio.csv','Data/prices.csv')
