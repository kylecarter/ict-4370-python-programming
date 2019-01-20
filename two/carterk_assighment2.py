'''
/**
 * Assignment 2 | ICT 4370 | Python Programming
 *
 * This represents the code work for addignment two. Note this project
 * was written for Python 3 Requirements:
 *
 * Use the following data table to create 4 lists – put stock symbols in
 * one list, number of shares in a second list, share purchase price in
 * the third and current share price for the fourth.  Make sure that you
 * keep the relative positions aligned. So if the Google stock symbol is
 * in the first slot on the first list, make sure that the quantity and
 * prices are in the other lists in the first slot as well.
 *
 * STOCK SYMBOL | NO SHARES | PURCHASE PRICE | CURRENT VALUE
 * _________________________________________________________
 * GOOGL        | 125       | 772.88         | 941.53
 * _________________________________________________________
 * MSFT         | 85        | 56.60          | 73.04
 * _________________________________________________________
 * RDS-A        | 400       | 49.58          | 55.74
 * _________________________________________________________
 * AIG          | 235       | 54.21          | 65.27
 * _________________________________________________________
 * FB           | 150       | 124.31         | 172.45
 *
 * Then create a report, similar to the one below, calculating how much the
 * investor has earned or lost.
 *
 * Stock ownership for Bob Smith
 *
 * -------------------------------------------------------------------------------
 * STOCK                        SHARE#                              EARNINGS/LOSS
 * -------------------------------------------------------------------------------
 * GOOGL                        125                                 $21026.25
 * MSFT                         85                                  $1397.4
 * RDS-A                        400                                 $2464
 * AIG                          235                                 $3599.1
 * FB                           150                                 $7221
 *
 * @category   Assignment
 * @package    AssignmentOne
 * @author     Kyle A. Carter <kyle.carter@du.edu>
 * @copyright  2019 Kyle A. Carter
 * @license    https://opensource.org/licenses/GPL-3.0  GNU General Public License version 3
 * @version    Git: 1.0.0
 * @link       https://github.com/kylecarter/ict-4370-python-programming
 * 
 */
'''

import locale
from decimal import Decimal

# Run using Python 3 will not work with Python 2

# This class is used to hold all the data and methods related to this project.
class StockInfo:

    # Creates initial variables.
    def __init__(self):
        self.locale = locale.getdefaultlocale()
        self.symbols = ['GOOGL', 'MSFT', 'RDS-A', 'AIG', 'FB']
        self.shares = [125, 85, 400, 235, 150]
        self.prices = [772.88, 56.60, 49.58, 54.21, 124.31]
        self.values = [941.53, 73.04, 55.74, 65.27, 172.45]


    # This returns a locale currency string of the value a person has made or lost
    # from a stock purchase. Positive numbers are money earned; negative values are
    # money lost.
    def get_stock_risk(self, purchase_price, current_price, num_shares):
        return self.get_local_currency((current_price * num_shares) - (purchase_price * num_shares))


    # Converts a number value to a localized currency string this uses the
    # client computer localization data to construct the string.
    def get_local_currency(self, currency):
        locale.setlocale(locale.LC_ALL, self.locale[0] + '.' + self.locale[1])
        return locale.currency(currency, grouping = True)
    

    # Creates spaces for pretty printing the data this uses the length of a table
    # header offset by the length of the previous cell value.
    def get_spaces(self, offset, count):
        spaces = ''
        for v in range(0, count + offset):
            spaces += ' '
        return spaces


    # Prints the data provided in the __init__ function as requested by the assignment
    #requirements
    def print_report(self):
        spaces = ''
        for z in range(0, 24):
            spaces += ' '
        
        header = 'STOCK' + spaces + 'SHARE#' + spaces + 'EARNINGS/LOSS'
        header_len = len(header)

        divider = ''
        for y in range(0, header_len):
            divider += '-'

        print(divider)
        print(header)
        print(divider)

        for x in range(0, len(self.symbols)):
            print(self.symbols[x] + self.get_spaces(len('STOCK') - len(self.symbols[x]), len(spaces)) + 
                str(self.shares[x]) + self.get_spaces(len('SHARE#') - len(str(self.shares[x])), len(spaces)) +
                self.get_stock_risk(
                    self.prices[x],
                    self.values[x],
                    self.shares[x])
                )


assignment2 = StockInfo()
assignment2.print_report()
