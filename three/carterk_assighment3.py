'''
/**
 * Assignment 3 | ICT 4370 | Python Programming
 *
 * This represents the code work for addignment two. Note this project
 * was written for Python 3. Requirements:
 *
 * This assignment will provide practice evaluating, selecting, and using
 * dictionaries and loops.
 *
 * Convert the assignment you created in lesson 3 to a solution that uses
 * dictionaries instead of lists. Keep in mind you can nest lists in 
 * dictionaries, dictionaries in lists and lists in lists. Think about the
 * data structure that makes most sense in this problem. Take into account
 * that you may eventually need to keep track of multiple investors.
 *
 * Write a short paragraph explaining which data structure is better to use
 * in this scenario – list(s) or dictionary(ies).
 *
 * As a part of best programming practices include code comments, at the
 * minimum a header with your name, the date the program was written and a
 * short description.
 *
 * @category   Assignment
 * @package    AssignmentThree
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
        locale.setlocale(locale.LC_ALL, self.locale[0] + '.' + self.locale[1])

        spaces = ''.join([' ' for x in range(0, 24)])
        headings = (
            'STOCK',
            'SHARE#',
            'EARNINGS/LOSS'
        )
        self.header = [heading + spaces for heading in headings]
        self.divider = ''.join(['-' for y in range(0, len(''.join(self.header)))])

        self.dataset = (
            {
                'stock_name': 'GOOGL',
                'num_shares': 125,
                'costs': {
                    'purchase_amount': '$772.88',
                    'current_price': '$941.53'
                }
            },
            {
                'stock_name': 'MSFT',
                'num_shares': 85,
                'costs': {
                    'purchase_amount': '$56.60',
                    'current_price': '$73.04'
                }
            },
            {
                'stock_name': 'RDS-A',
                'num_shares': 400,
                'costs': {
                    'purchase_amount': '$49.58',
                    'current_price': '$55.74'
                }
            },
            {
                'stock_name': 'AIG',
                'num_shares': 235,
                'costs': {
                    'purchase_amount': '$54.21',
                    'current_price': '$65.27'
                }
            },
            {
                'stock_name': 'FB',
                'num_shares': 150,
                'costs': {
                    'purchase_amount': '$124.31',
                    'current_price': '$172.45'
                }
            },
        )

    # Creates and output string for each dataset.
    def get_output(self, data):
        output = ''
        num_shares = float(0)

        for key, value in data.items():
            if key == 'stock_name' and isinstance(value, str):
                output += value.upper() + self.get_spaces(
                    len(self.header[0]) - len(value))
            
            if key == 'num_shares':
                if isinstance(value, int) or isinstance(value, float):
                    output += str(value) + self.get_spaces(
                        len(self.header[1]) - len(str(value)))
                    num_shares = value

            if key == 'costs':
                purchase_amount = float(0)
                try:
                    purchase_amount = self.convert_to_number(
                        data[key]['purchase_amount'])
                except:
                    pass

                current_price = float(0)
                try:
                    current_price = self.convert_to_number(
                        data[key]['current_price'])
                except:
                    pass
                
                output += self.get_stock_risk(purchase_amount, current_price, num_shares)

        return output

    # Takes the user input for the value of the stocks and converts them to number
    # strings. This takes into account if the user is entering currency for their
    # locale.
    def convert_to_number(self, currency):
        return locale.atof(currency.strip(locale.localeconv()['currency_symbol']))

    # This returns a locale currency string of the value a person has made or lost
    # from a stock purchase. Positive numbers are money earned; negative values are
    # money lost.

    def get_stock_risk(self, purchase_price, current_price, num_shares):
        return self.get_local_currency((current_price * num_shares) - (purchase_price * num_shares))

    # Converts a number value to a localized currency string this uses the
    # client computer localization data to construct the string.

    def get_local_currency(self, currency):
        locale.setlocale(locale.LC_ALL, self.locale[0] + '.' + self.locale[1])
        return locale.currency(currency, grouping=True)

    # Creates spaces for pretty printing the data this uses the length of a table
    # header offset by the length of the previous cell value.

    def get_spaces(self, offset):
        return ''.join([' ' for v in range(0, offset)])

    # Prints the data provided in the __init__ function as requested by the assignment
    #requirements

    def print_report(self):
        output = [self.get_output(stock) for stock in self.dataset]

        if len(output) > 0:
            print(self.divider)
            print(''.join(self.header))
            print(self.divider)

            for info in output:
                print(info)
        else:
            print('Nothing to see here.')

assignment3 = StockInfo()
assignment3.print_report()

''' Note
I find for both and lists and dictionaries are useful for this application
scenario. In meaning, a list of dictionaries is the best approach here. The
static data provided for this assignment resembles the common query set results
that would come from a database query. Typically query sets are some sort of
list (either a tuple or list; probably a tuple because you don't want the program
altering the original dataset). From there the list will contain a collection of
dictionaries that provide key/value pairs for the individual data points in the
query set.

To break this down further, lists are good for large chuncks of commonly structured
data points. That is they work well with data that is all of the same type. From
there dictionaries work well with data that has similar structure but varying values.
This all said it is best to group the data provided here in a list of dictionaries
and then iterate over the list to process the individual dictionaries that represent
the individual data points.
'''
