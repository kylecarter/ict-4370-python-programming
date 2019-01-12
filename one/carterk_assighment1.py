'''
/**
 * Assignment 1 | ICT 4370 | Python Programming
 *
 * This represents the code work for addignment one. Note this project
 * was written for Python 3 Requirements:
 *
 * Create a program that will ask the user for their name, a stock symbol for
 * the stock they own (for example for Google that would be GOOGL), how many
 * shares they own, what price they bought it at, and its current price.
 * Calculate how much money they earned or lost. The output should look
 * something like this:
 *
 * Stock ownership for Bob Smith
 * ----------------------------------------------------
 * GOOGL: 125 shares
 * Purchase Price: 772.88
 * Current Price per Share: 941.53
 * Earnings/Loss to-date: $21081.25
 *
 * This assignment will provide you with the opportunity to break down a task
 * with a specific business need into programmable tasks. While working on this
 * assignment, you will have the opportunity to practice working with different
 * types of variables, simple math operations and print statements.
 *
 * As a part of best programming practices, include code comments, at the
 * minimum a header with your name, the date the program was written and a
 * short description.
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

class StockInfo:

    def __init__(self):
        self.stock_name = ''
        self.num_shares = float(0)
        self.cost_per_share = float(0)
        self.current_cost_per_share = float(0)
        self.locale = locale.getdefaultlocale()

    def get_data(self):
        return {
            'stock_name': input("Please enter a stock symbol you own: "),
            'num_shares': input(
                "How many shares of this stock do you own? "),
            'cost_per_share': input(
                "How much did you pay for each share? "),
            'current_cost_per_share': input(
                "How much do the shares cost now? ")
        }

    def valid(self, data):
        valid = True
        self.stock_name = data['stock_name']

        try:
            self.num_shares = float(data['num_shares'])
        except:
            valid = False
        
        try:
            self.cost_per_share = self.convert_to_number(
                data['cost_per_share'])
        except:
            valid = False

        try:
            self.current_cost_per_share = self.convert_to_number(
                data['current_cost_per_share'])
        except:
            valid = False

        return valid

    def convert_to_number(self, currency):
        locale.setlocale(locale.LC_ALL, self.locale[0] + '.' + self.locale[1])
        conv = locale.localeconv()
        return locale.atof(currency.strip(conv['currency_symbol']))

    def get_stock_risk(self, purchase_price, current_price):
        return self.get_local_currency(purchase_price - current_price)

    def get_local_currency(self, currency):
        return str(currency)

    def show_data(self):
        data = self.get_data()

        if self.valid(data):
            print(self.stock_name.upper() + ': ' + str(self.num_shares))
            print('Purchase Price: ' + self.get_local_currency(self.cost_per_share))
            print('Current Price per Share: ' +
                  self.get_local_currency(self.current_cost_per_share))
            print('Earnings/Loss to-date: ' +
                self.get_stock_risk(self.cost_per_share, self.current_cost_per_share))
        else:
            print('There were issues with the data you entered. Please review your data entries.')

assignment1 = StockInfo()
assignment1.show_data()
