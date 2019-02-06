'''
/**
 * Assignment 5 | ICT 4370 | Python Programming
 *
 * Converts a number to a local currency string.
 *
 * @category   Assignment
 * @package    AssignmentFiveStock
 * @author     Kyle A. Carter <kyle.carter@du.edu>
 * @copyright  2019 Kyle A. Carter
 * @license    https://opensource.org/licenses/GPL-3.0  GNU General Public License version 3
 * @version    Git: 1.0.0
 * @link       https://github.com/kylecarter/ict-4370-python-programming
 * 
 */
'''

import calendar
import locale

from datetime import datetime, date


class Stock():

    def __init__(self):
        """
        Sets the initial variables. These are used for printing content
        and storing initial data.
        """
        self.locale = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, '')

        self.spaces = ''.join([' ' for x in range(0, 24)])
        self.headings = (
            'STOCK',
            'SHARE#',
            'EARNINGS/LOSS',
            'YEARLY EARNING/LOSS'
        )
        self.header = [heading + self.spaces for heading in self.headings]
        self.divider = ''.join(
            ['-' for y in range(0, len(''.join(self.header)))])

        self.dataset = (
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

    def get_local_currency(self, currency):
        """
        Converts a number value to a localized currency string this uses the
        client computer localization data to construct the string.
        """
        return locale.currency(currency, grouping=True)


    def convert_to_number(self, currency):
        """
        Takes the user input for the value of the stocks and converts them to number
        strings. This takes into account if the user is entering currency for their
        locale.
        """
        return locale.atof(currency.strip(locale.localeconv()['currency_symbol']))

    def get_spaces(self, offset):
        """
        Creates spaces for pretty printing the data this uses the length of a table
        header offset by the length of the previous cell value.
        """
        return ''.join([' ' for v in range(0, offset)])

    def print_stock_details(self):
        header = self.header

        print(self.divider)
        print(''.join(header))
        print(self.divider)

        for stock in self.dataset:
            output = ''

            output += stock['stock_name'] + self.get_spaces(
                len(header[0]) - len(stock['stock_name']))
            
            output += str(stock['num_shares']) + self.get_spaces(
                len(header[1]) - len(str(stock['num_shares'])))

            risk = self.get_risk(stock['costs']['purchase_amount'],
                stock['costs']['current_price'], stock['num_shares'])

            output += risk + self.get_spaces(
                len(header[2]) - len(risk))

            risk_percent = self.get_risk_percent(purchase_price = stock['costs']['purchase_amount'],
                current_price = stock['costs']['current_price'], purchased = stock['purchased'])

            output += risk_percent + self.get_spaces(
                len(header[3]) - len(risk_percent))

            print(output)

    def get_risk(self, purchase_price, current_price, num_shares):
        """
        This returns a locale currency string of the value a person has made or lost
        from a stock purchase. Positive numbers are money earned; negative values are
        money lost.
        """
        return self.get_local_currency(
            (self.convert_to_number(current_price) - self.convert_to_number(purchase_price)) * num_shares
        )

    def get_risk_percent(self, **data):
        """
        This returns a percentage representing the yearly earnings/loss
        percent.
        """

        DAY_TO_YEAR = .00273973
        date_format = '%Y-%m-%d'
        date_now = datetime.strptime(
            date.today().strftime(date_format), date_format)
        date_then = datetime.strptime(data['purchased'], date_format)
        date_delta = (date_now - date_then).days * DAY_TO_YEAR

        current_price = self.convert_to_number(data['current_price'])
        purchase_price = self.convert_to_number(data['purchase_price'])
        price_difference = current_price - purchase_price

        return '{0:.2f}%'.format(
            ((price_difference / purchase_price) / date_delta) * 100
        )
