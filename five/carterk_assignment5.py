'''
/**
 * Assignment 5 | ICT 4370 | Python Programming
 *
 * Using the previous assignment, set up your code to use classes. Set up the
 * stock data variables as class attributes and functions as stock class methods.
 *
 * Create a class for the investor as well, and add an address and phone number
 * component for them.
 *
 * Create an additional class for bonds. Bonds are similar to stocks, so set up
 * the bond class to inherit from the stock class, but add coupon and yield 
 * attributes to it as well. Add method necessary to read the additional
 * two values.
 *
 * Add ID fields in all the classes – for example investorID for the investor
 * class and purchaseID for the stock and bond purchase records.
 *
 * Instantiate all the classes to the current information Bob Smith has.
 *
 * Add a single bond to Bob Smith’s portfolio, with the following information:
 *
 * Symbol: GT2:GOV
 * Purchase Price: 100.02
 * Current Price: 100.05
 * Quantity: 200
 * Coupon: 1.38
 * Yield: 1.35%
 * Purchase Date: 8/1/2017
 *
 * Create a screen print out, just like you did before, but also add a bond section.
 *
 *
 * @category   Assignment
 * @package    AssignmentFive
 * @author     Kyle A. Carter <kyle.carter@du.edu>
 * @copyright  2019 Kyle A. Carter
 * @license    https://opensource.org/licenses/GPL-3.0  GNU General Public License version 3
 * @version    Git: 1.0.0
 * @link       https://github.com/kylecarter/ict-4370-python-programming
 * 
 */
'''

# Run using Python 3 will not work with Python 2
from carterk_assignment5_stock import Stock


print('Initial data:')
assignment5 = Stock()
assignment5.print_stock_details()
# assignment5.set_stock({
#     'stock_name': 'GT2:GOV',
#     'num_shares': 200,
#     'costs': {
#         'purchase_amount': '$100.02',
#         'current_price': '$100.05'
#     },
#     'purchased': '2017-08-01'
# })