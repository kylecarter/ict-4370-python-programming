'''
/**
 * Assignment 4 | ICT 4370 | Python Programming
 *
 * This represents the code work for addignment two. Note this project
 * was written for Python 3. Requirements:
 *
 * This assignment will provide you with practice creating functions and
 * determining how and when to use them.
 *
 * Using the previous assignment, move the code you use to calculate the
 * loss/gain into a function.
 *
 * Furthermore, add an additional data item - the purchase date. Make sure
 * that each of the existing entries has the purchase date of 8/1/2015. Then
 * add the following two records as well.
 *
 * Add a second function to your code that calculates the percentage yield/loss
 * for each of the stocks, and a third that will calculate the yearly earnings/loss
 * rate (the formulas are below).
 *
 * Move all your functions to a separate module.
 *
 * STOCK SYMBOL | NO SHARES | PURCHASE PRICE | CURRENT VALUE | PURCHASE DATE
 * __________________________________________________________________________
 * M            | 425       | 30.30          | 23.98         | 1/10/2017
 * __________________________________________________________________________
 * F            | 85        | 12.58          | 10.95         | 2/17/2017
 * __________________________________________________________________________
 * IBM          | 80        | 150.37         | 145.30        | 5/12/2017
 *
 * Then create a report, similar to the one below, calculating how much the investor
 * has earned or lost, as well as the average yearly return.
 *
 * Calculate the earnings/loss by using the following formula:
 * - (current value – purchase price) x number of shares
 *
 * Calculate yearly earnings/loss rate using the following formula*:
 * - ((((current value – purchase price)/purchase price)/(current date – purchase date)))*100
 *
 * *for anyone with a finance background, while this may not be the best way to calculate the
 * average yearly yield, it will serve the purpose for this exercise.
 *
 * --------------------------------------------------------------------------------------------------------------------------------
 * STOCK                        SHARE#                              EARNINGS/LOSS                              YEARLY EARNING/LOSS
 * --------------------------------------------------------------------------------------------------------------------------------
 * M                            425                                 -$2686.00                                  -37.32% 
 * F                             85                                  -$135.55                                  -28.49%
 * IBM                           80                                  -$405.60                                  -15.01%
 *
 * @category   Assignment
 * @package    AssignmentFour
 * @author     Kyle A. Carter <kyle.carter@du.edu>
 * @copyright  2019 Kyle A. Carter
 * @license    https://opensource.org/licenses/GPL-3.0  GNU General Public License version 3
 * @version    Git: 1.0.0
 * @link       https://github.com/kylecarter/ict-4370-python-programming
 * 
 */
'''

# Run using Python 3 will not work with Python 2
from carterk_assignment4_earningsloss import get_risk
from carterk_assignment4_earningsloss_yearly import get_risk_percent


dataset = (
    {
        'stock_name': 'GOOGL',
        'num_shares': 125,
        'costs': {
            'purchase_amount': '$772.88',
            'current_price': '$941.53'
        },
        'purchased': '2015-08-1'
    },
    {
        'stock_name': 'MSFT',
        'num_shares': 85,
        'costs': {
            'purchase_amount': '$56.60',
            'current_price': '$73.04'
        },
        'purchased': '2015-08-1'
    },
    {
        'stock_name': 'RDS-A',
        'num_shares': 400,
        'costs': {
            'purchase_amount': '$49.58',
            'current_price': '$55.74'
        },
        'purchased': '2015-08-1'
    },
    {
        'stock_name': 'AIG',
        'num_shares': 235,
        'costs': {
            'purchase_amount': '$54.21',
            'current_price': '$65.27'
        },
        'purchased': '2015-08-1'
    },
    {
        'stock_name': 'FB',
        'num_shares': 150,
        'costs': {
            'purchase_amount': '$124.31',
            'current_price': '$172.45'
        },
        'purchased': '2015-08-1'
    },
    {
        'stock_name': 'M',
        'num_shares': 425,
        'costs': {
            'purchase_amount': '$30.30',
            'current_price': '$23.98'
        },
        'purchased': '2017-01-10'
    },
    {
        'stock_name': 'F',
        'num_shares': 85,
        'costs': {
            'purchase_amount': '$12.58',
            'current_price': '$10.95'
        },
        'purchased': '2017-02-17'
    },
    {
        'stock_name': 'IBM',
        'num_shares': 80,
        'costs': {
            'purchase_amount': '$150.37',
            'current_price': '$145.30'
        },
        'purchased': '2017-05-12'
    },
)

def get_spaces(offset):
    """
    Creates spaces for pretty printing the data this uses the length of a table
    header offset by the length of the previous cell value.
    """
    return ''.join([' ' for v in range(0, offset)])


spaces = ''.join([' ' for x in range(0, 24)])
headings = (
    'STOCK',
    'SHARE#',
    'EARNINGS/LOSS',
    'YEARLY EARNING/LOSS'
)
header = [heading + spaces for heading in headings]
divider = ''.join(
    ['-' for y in range(0, len(''.join(header)))])

# Output from the processes here.
print(divider)
print(''.join(header))
print(divider)

for stock in dataset:
    output = ''

    output += stock['stock_name'] + get_spaces(
        len(header[0]) - len(stock['stock_name']))
    
    output += str(stock['num_shares']) + get_spaces(
        len(header[1]) - len(str(stock['num_shares'])))

    risk = get_risk(stock['costs']['purchase_amount'],
        stock['costs']['current_price'], stock['num_shares'])

    output += risk + get_spaces(
        len(header[2]) - len(risk))

    risk_percent = get_risk_percent(purchase_price = stock['costs']['purchase_amount'],
        current_price = stock['costs']['current_price'], purchased = stock['purchased'])

    output += risk_percent + get_spaces(
        len(header[3]) - len(risk_percent))

    print(output)
