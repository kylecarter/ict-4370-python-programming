'''
/**
 * Assignment 7 | ICT 4370 | Python Programming
 *
 * Use the assignment created in the previous lesson. Use the data you read
 * into your data structures from the text files and write it to the database.
 * You can use either the dictionary data structure or the class data
 * structure you set up in previous assignments. Use the header names for
 * database attribute names as you are setting up the database. In addition to
 * those fields, add a investor_id field to the investor table, stock_id and
 * the related investor_id field to the stock table, and bond_id and related
 * investor_id to the bond table.
 *
 * Write code that will retrieve the data into your data structures, and print
 * it out, in the same format as we used in the previous assignments.  
 *
 * Make sure your code is set up to handle exceptions.
 *
 * @category   Assignment
 * @package    AssignmentSeven
 * @author     Kyle A. Carter <kyle.carter@du.edu>
 * @copyright  2019 Kyle A. Carter
 * @license    https://opensource.org/licenses/GPL-3.0  GNU General Public License version 3
 * @version    Git: 1.0.0
 * @link       https://github.com/kylecarter/ict-4370-python-programming
 * 
 */
'''

# Run using Python 3 will not work with Python 2
import json
import os

from carterk_assignment7_investor import Investor
from carterk_assignment7_model import InvestorModel

# model = InvestorModel()
def process_assignment7(data, __dirname):
    '''
    Takes a JSON file loaded from a computer and outputs the data
    using the classes provided to process the data. Accepts a absolute
    system path for finding and outputing a file.
    '''
    assignment7_investors = []
    for investor in data['investors']:
        assignment7 = Investor(
            first_name=investor['first_name'],
            middle_name=investor['middle_name'],
            last_name=investor['last_name'],
            street=investor['street'],
            street_2=investor['street_2'],
            city=investor['city'],
            state=investor['state'],
            postal_code=investor['postal_code'],
            phone_number=investor['phone_number'],
            email=investor['email']
        )

        for stock in investor['stocks']:
            assignment7.set_stock_ownership(
                stock_name=stock['stock_name'],
                num_shares=stock['num_shares'],
                purchased=stock['purchased'],
                investor=assignment7.id,
                purchase_amount=stock['costs']['purchase_amount'],
                current_price=stock['costs']['current_price']
            )

        for bond in investor['bonds']:
            assignment7.set_bond_ownership(
                stock_name=bond['stock_name'],
                num_shares=bond['num_shares'],
                purchased=bond['purchased'],
                investor=assignment7.id,
                purchase_amount=bond['costs']['purchase_amount'],
                current_price=bond['costs']['current_price'],
                coupon=bond['coupon'],
                bond_yield=bond['bond_yield']
            )
        
        assignment7_investors.append(assignment7)

    with open(os.path.join(__dirname, 'carterk_assignment7.md'), 'w+') as f:
        title = 'Investor Details\n'
        f.write(title)
        f.write(''.join(['=' for x in range(0, len(title))]) + '\n')

        for investor in assignment7_investors:
            investor_title = investor.get_investor_full_name(
                investor.first_name,
                investor.middle_name,
                investor.last_name
            ).title()
            f.write(investor_title + '\n')
            f.write(''.join(['-' for x in range(0, len(investor_title))]) + '\n')

            f.write('### Contact\n')
            investor_address = investor.get_investor_address(
                street=investor.street,
                street_2=investor.street_2,
                city=investor.city,
                state=investor.state,
                postal_code=investor.postal_code,
            )

            for x in range(0, len(investor_address)):
                f.write('* ' + investor_address[x] + '\n')

            f.write('* ' + investor.get_investor_phone_num() + '\n')
            
            f.write('### Stocks\n')
            f.write(investor.print_stock_details())

            f.write('### Bonds\n')
            f.write(investor.print_bond_details())

# Actual program processor. The carterk_assignment7.json must be in the same directory
# as the carterk_assignment7.py in order for this program to work.
dirname, filename = os.path.split(os.path.abspath(__file__))
try:
    with open(os.path.join(dirname, 'carterk_assignment7.json')) as data:
        process_assignment7(json.load(data), dirname)
except FileNotFoundError as notfound:
    print('There is no data to process.')