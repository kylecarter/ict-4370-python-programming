'''
/**
 * Assignment 6 | ICT 4370 | Python Programming
 *
 * Class for stock and bonds owners.
 *
 * @category   Assignment
 * @package    AssignmentSixOwner
 * @author     Kyle A. Carter <kyle.carter@du.edu>
 * @copyright  2019 Kyle A. Carter
 * @license    https://opensource.org/licenses/GPL-3.0  GNU General Public License version 3
 * @version    Git: 1.0.0
 * @link       https://github.com/kylecarter/ict-4370-python-programming
 * 
 */
'''
import uuid

from carterk_assignment6_stock import Stock
from carterk_assignment6_bond import Bond


class Owner():
    """
    This class represents the owner of a stocks and bonds.
    """

    def __init__(self, **kwargs):
        """
        Represents the owner of a collection of stocks and bonds.
        Sets a UUID for the owner and sets any data provided by the
        application about the owner.
        """
        self.id = str(uuid.uuid1())
        self.stocks = []
        self.bonds = []
        
        for name, value in kwargs.items():
            self.__setattr__(name, value)


    def __setattr__(self, name, value):
        """
        Sets named attributes to a class object.
        """
        self.__dict__[name] = value


    def set_stock_ownership(self, **kwargs):
        """
        Adds an owned stock to the class instance list
        """
        self.stocks.append(Stock(**kwargs))


    def set_bond_ownership(self, **kwargs):
        """
        Adds an owned bond to the class instance list
        """
        self.bonds.append(Bond(**kwargs))


    def get_owner_full_name(self, *args):
        """
        Given a list of strings will return a concatnated
        name string.
        """
        return ' '.join(args)


    def get_owner_address(self, **kwargs):
        """
        Given a collection of keyword arguments will return the
        values as a list of information.
        """
        address = []

        if kwargs['street']:
            address.append(kwargs['street'])
        
        if kwargs['street_2']:
            address.append(kwargs['street_2'])
        
        city_state = []
        address_details = ''
        if kwargs['city']:
            city_state.append(kwargs['city'])
        
        if kwargs['state']:
            city_state.append(kwargs['state'])
        
        address_details = ', '.join(city_state)
        
        if kwargs['postal_code']:
            address_details += ' ' + kwargs['postal_code']
        
        if len(address_details.strip()) > 0:
            address.append(address_details.strip())
        
        return address


    def get_owner_phone_num(self):
        if not self.phone_number:
            return '(p)' + ' Unavailable'
        else:
            return '(p)' + self.phone_number
    

    def print_stock_details(self):
        output = ''
        headings = (
            'STOCK',
            'SHARE#',
            'EARNINGS/LOSS',
            'YEARLY EARNING/LOSS'
        )
        spaces = ''.join([' ' for x in range(0, len(headings) - 1)])
        header = '| ' + ''.join([heading.upper() + spaces + ' | ' for heading in headings]) + '\n'
        divider = '|'
        for heading in headings:
            divider += ':' + ''.join(['-' for x in range(0, len(heading + spaces))]) + ' |'
        
        output += header + divider + '\n'

        for stock in self.stocks:
            output += stock.print_output_row(headings, spaces)
        
        return output


    def print_bond_details(self):
        output = ''
        headings = (
            'STOCK',
            'SHARE#',
            'EARNINGS/LOSS',
            'YEARLY EARNING/LOSS',
            'COUPON',
            'YIELD'
        )
        spaces = ''.join([' ' for x in range(0, len(headings) - 1)])
        header = '| ' + ''.join([heading.upper() + spaces + ' | ' for heading in headings]) + '\n'
        divider = '|'
        for heading in headings:
            divider += ':' + ''.join(['-' for x in range(0, len(heading + spaces))]) + ' |'
        
        output += header + divider + '\n'

        for bond in self.bonds:
            output += bond.print_output_row(headings, spaces)

        return output + '\n'
