'''
/**
 * Assignment 7 | ICT 4370 | Python Programming
 *
 * Class connecting to the Database.
 *
 * @category   Assignment
 * @package    AssignmentSevenDB
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


class Model():
    """
    A generic class for manageing database models. Meant to be inherited
    by other model classes to manage themselves.
    """

    def __init__(self, model):
        self.table = "carterk_assignment7_"
        print(model)
        print(self.__class__.lower())


class InvestorModel(Model):
    """
    A database model for the Investor object.
    """

    def __init__(self):
        super().__init__(self.__dict__)
        self.first_name = {
            'type': 'text',
            'can_be_empty': False
        }
        self.middle_name = {
            'type': 'text',
            'can_be_empty': True
        }
        self.last_name = {
            'type': 'text',
            'can_be_empty': False
        }
        self.street = {
            'type': 'text',
            'can_be_empty': True
        }
        self.street2 = {
            'type': 'text',
            'can_be_empty': True
        }
        self.city = {
            'type': 'text',
            'can_be_empty': True
        }
        self.state = {
            'type': 'text',
            'can_be_empty': True
        }
        self.postal_code = {
            'type': 'text',
            'can_be_empty': True
        }
        self.phone_number = {
            'type': 'text',
            'can_be_empty': True
        }
        self.email = {
            'type': 'text',
            'can_be_empty': True
        }
