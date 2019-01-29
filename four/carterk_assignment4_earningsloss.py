'''
/**
 * Assignment 4 | ICT 4370 | Python Programming
 *
 * Calculates the earnings/loss from a stock based on the following formula:
 * - (current value – purchase price) x number of shares
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

from carterk_assignment4_currency import get_local_currency, convert_to_number


def get_risk(purchase_price, current_price, num_shares):
    """
    This returns a locale currency string of the value a person has made or lost
    from a stock purchase. Positive numbers are money earned; negative values are
    money lost.
    """
    return get_local_currency(
        (convert_to_number(current_price) - convert_to_number(purchase_price)) * num_shares
    )
