'''
/**
 * Assignment 5 | ICT 4370 | Python Programming
 *
 * Class for Bonds.
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
import uuid

from carterk_assignment5_stock import Stock

class Bond(Stock):
    """
    A class for managing bonds.
    """

    def __init__(self, coupon=None, bond_yield=None, **kwargs):
        """
        Sets the initial variables. These are used for printing content
        and storing initial data.
        """
        super().__init__(**kwargs)
        self.id = str(uuid.uuid1())
        self.coupon = coupon
        self.bond_yield = bond_yield

        for name, value in kwargs.items():
            self.__setattr__(name, value)


    def print_output_row(self, header):
        """
        Prints individual rows of bond data.
        """
        output = ''

        output += self.stock_name + self.get_spaces(
            len(header[0]) - len(self.stock_name))
        
        output += str(self.num_shares) + self.get_spaces(
            len(header[1]) - len(str(self.num_shares)))

        risk = self.get_risk(self.purchase_amount,
            self.current_price, self.num_shares)
        output += risk + self.get_spaces(
            len(header[2]) - len(risk))

        risk_percent = self.get_risk_percent(purchase_price=self.purchase_amount,
            current_price=self.current_price, purchased=self.purchased)
        output += risk_percent + self.get_spaces(
            len(header[3]) - len(risk_percent))
        
        output += str(self.coupon) + self.get_spaces(
            len(header[4]) - len(str(self.coupon)))

        printable_yield = '{0:.2f}%'.format(self.bond_yield)
        output += printable_yield + self.get_spaces(
            len(header[5]) - len(printable_yield))

        print(output)
