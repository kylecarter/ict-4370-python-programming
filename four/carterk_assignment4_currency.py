'''
/**
 * Assignment 4 | ICT 4370 | Python Programming
 *
 * Converts a number to a local currency string.
 *
 * @category   Assignment
 * @package    AssignmentFourCurrency
 * @author     Kyle A. Carter <kyle.carter@du.edu>
 * @copyright  2019 Kyle A. Carter
 * @license    https://opensource.org/licenses/GPL-3.0  GNU General Public License version 3
 * @version    Git: 1.0.0
 * @link       https://github.com/kylecarter/ict-4370-python-programming
 * 
 */
'''

import locale


system_locale = locale.getdefaultlocale()
locale.setlocale(locale.LC_ALL, system_locale[0] + '.' + system_locale[1])


def get_local_currency(currency):
    """
    Converts a number value to a localized currency string this uses the
    client computer localization data to construct the string.
    """
    return locale.currency(currency, grouping=True)


def convert_to_number(currency):
    """
    Takes the user input for the value of the stocks and converts them to number
    strings. This takes into account if the user is entering currency for their
    locale.
    """
    return locale.atof(currency.strip(locale.localeconv()['currency_symbol']))
