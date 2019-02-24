'''
/**
 * Assignment 7 | ICT 4370 | Python Programming
 *
 * Class for Stocks.
 *
 * @category   Assignment
 * @package    AssignmentSevenStock
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


class Stock():
    """
    A class for managing Stock data.
    """

    def __init__(self, **kwargs):
        """
        Sets the initial variables. These are used for printing content
        and storing initial data.
        """
        self.id = str(uuid.uuid1())
        self.locale = locale.getdefaultlocale()
        locale.setlocale(locale.LC_ALL, '')

        for name, value in kwargs.items():
            self.__setattr__(name, value)


    def __setattr__(self, name, value):
        """
        Sets named attributes to a class object.
        """
        self.__dict__[name] = value


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

    def print_output_row(self, headings, spaces):
        """
        Prints individual rows of stock data.
        """
        output = '| '

        output += self.stock_name.upper() + self.get_spaces(
            len(headings[0] + spaces) - len(self.stock_name)) + ' | '
        
        output += str(self.num_shares) + self.get_spaces(
            len(headings[1] + spaces) - len(str(self.num_shares))) + ' | '

        risk = self.get_risk(self.purchase_amount,
            self.current_price, self.num_shares)

        output += risk + self.get_spaces(
            len(headings[2] + spaces) - len(risk)) + ' | '

        risk_percent = self.get_risk_percent(purchase_price=self.purchase_amount,
            current_price=self.current_price, purchased=self.purchased)

        output += risk_percent + self.get_spaces(
            len(headings[3] + spaces) - len(risk_percent)) + ' | '

        return output + '\n'

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
