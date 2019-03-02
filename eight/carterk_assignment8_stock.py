'''
/**
 * Assignment 8 | ICT 4370 | Python Programming
 *
 * Class for Stocks.
 *
 * @category   Assignment
 * @package    AssignmentEightStock
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
import uuid

from datetime import datetime, date

class Stock:

    def __init__(self, **kwargs):
        """
        Sets up the stock object with the values provided to the Class at
        creation of the object.

        @param {dict} kwargs a collection of data values from the json
        """
        self.symbol = kwargs['symbol']

        try:
            date_format = '%d-%b-%y'
            self.date = datetime.strptime(kwargs['date'], date_format)
        except ValueError as identifier:
            self.date = None
            print("Date data {} does not match format '%d-%b-%y'").format(kwargs['date'])

        try:
            self.open = float(kwargs['open'])
        except ValueError as identifier:
            self.open = 0

        try:
            self.high = float(kwargs['high'])
        except ValueError as identifier:
            self.high = 0

        try:
            self.low = float(kwargs['low'])
        except ValueError as identifier:
            self.low = 0

        try:
            self.close = float(kwargs['close'])
        except ValueError as identifier:
            self.close = 0

        try:
            self.volume = int(kwargs['volume'])
        except ValueError as identifier:
            self.volume = 0


    def get_local_currency(self, currency):
        """
        Converts a number value to a localized currency string this uses the
        client computer localization data to construct the string.

        @param {dict} self current class instance
        @param {str} currency number to convert to a local currency string
        @return {str} a localized currency string
        """
        return locale.currency(currency, grouping=True)


    def convert_to_number(self, numstr):
        """
        Takes the user input for the value of the stocks and converts them to number
        strings. This takes into account if the user is entering currency for their
        locale.

        @param {dict} self current class instance
        @param {str} numstr number string
        @return {str} a localized currency string
        """
        return locale.atof(numstr.strip(locale.localeconv()['currency_symbol']))


    def get_risk(self):
        """
        This returns a locale currency string of the value a person has made or lost
        from a stock purchase. Positive numbers are money earned; negative values are
        money lost.

        @param {dict} self current class instance
        @return {str} a localized currency string
        """
        return self.get_local_currency(
            (self.convert_to_number(self.current_price) -
             self.convert_to_number(self.purchase_price)) * self.num_shares
        )


    def get_risk_percent(self):
        """
        This returns a percentage representing the yearly earnings/loss
        percent.

        @param {dict} self current class instance
        @return {str} a decimal value percent rounded to two decimal points
        """

        DAY_TO_YEAR = .00273973
        date_format = '%Y-%m-%d'
        date_now = datetime.strptime(
            date.today().strftime(date_format), date_format)
        date_then = datetime.strptime(self.purchased, date_format)
        date_delta = (date_now - date_then).days * DAY_TO_YEAR

        current_price = self.convert_to_number(self.current_price)
        purchase_price = self.convert_to_number(self.purchase_price)
        price_difference = current_price - purchase_price

        return '{0:.2f}%'.format(
            ((price_difference / purchase_price) / date_delta) * 100
        )
