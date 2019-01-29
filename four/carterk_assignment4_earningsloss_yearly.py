'''
/**
 * Assignment 4 | ICT 4370 | Python Programming
 *
 * Calculates the yearly earnings/loss from a stock based on the following formula:
 * - ((((current value – purchase price)/purchase price)/(current date – purchase date)))*100
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

import calendar
from datetime import datetime, date

from carterk_assignment4_currency import convert_to_number

def get_risk_percent(**data):
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

    current_price = convert_to_number(data['current_price'])
    purchase_price = convert_to_number(data['purchase_price'])
    price_difference = current_price - purchase_price

    return '{0:.2f}%'.format(
        ((price_difference / purchase_price) / date_delta) * 100
    )
