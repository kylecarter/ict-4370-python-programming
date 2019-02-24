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

# Run using Python 3 with SQLite 3
import json
import os

from carterk_assignment7_investor import Investor
from carterk_assignment7_model import Investors, Stocks, Bonds

def assignment7_create_db(data, __dirname):
    '''
    Creates the project database and loads data from carterk_assignment7.json
    into database tables.

    @param {dict} data dict object from imported json
    @param {str} __dirname string of current path
    '''
    for person in data['investors']:
        investor = Investors(
            __dirname,
            'first_name',
            'middle_name',
            'last_name',
            'street',
            'street_2',
            'city',
            'state',
            'postal_code',
            'phone_number',
            'email'
        )

        if person['email']:
            financer = investor.get_one(email=person['email'])
            if not financer:
                financer = investor.set_one(person)

            if person['stocks']:
                for symbol in person['stocks']:
                    stock = Stocks(
                        __dirname,
                        financer['id'],
                        'stock_name',
                        'num_shares',
                        'purchase_amount',
                        'current_price',
                        'purchased'
                    )
                    invested = stock.get_one(investor=financer['id'],
                        stock_name=symbol['stock_name'], purchased=symbol['purchased'])
                    if not invested:
                        invested = stock.set_one_stock(symbol)
                    investor.update_stocks(financer['id'], invested['id'])

            if person['bonds']:
                for symbol in person['bonds']:
                    bond = Bonds(
                        __dirname,
                        financer['id'],
                        'stock_name',
                        'num_shares',
                        'purchase_amount',
                        'current_price',
                        'purchased',
                        'coupon',
                        'bond_yield'
                    )
                    invested = bond.get_one(investor=financer['id'],
                        stock_name=symbol['stock_name'], purchased=symbol['purchased'])
                    if not invested:
                        invested = bond.set_one_bond(symbol)
                    investor.update_bonds(financer['id'], invested['id'])

        else:
            print('Please provide an investor email for unique entries.')


def assignment7_create_output(data, __dirname):
    '''
    Takes a JSON file loaded from a computer and outputs the data
    using the classes provided to process the data. Accepts a absolute
    system path for finding and outputing a file.
    '''
    investors = Investors(__dirname)
    assignment7_investors = []
    for record in investors.get_all():
        investor = Investor(
            first_name=record['first_name'] if record['first_name'] else '',
            middle_name=record['middle_name'] if record['middle_name'] else '',
            last_name=record['last_name'] if record['last_name'] else '',
            street=record['street'] if record['street'] else '',
            street_2=record['street_2'] if record['street_2'] else '',
            city=record['city'] if record['city'] else '',
            state=record['state'] if record['state'] else '',
            postal_code=record['postal_code'] if record['postal_code'] else '',
            phone_number=record['phone_number'] if record['phone_number'] else '',
            email=record['email'] if record['email'] else ''
        )

        for stock in record['stocks'].split():
            invested = Stocks(__dirname, stock).get_one(id=stock)
            investor.set_stock_ownership(
                stock_name=invested['stock_name'],
                num_shares=invested['num_shares'],
                purchased=invested['purchased'],
                investor=record['id'],
                purchase_amount=invested['purchase_amount'],
                current_price=invested['current_price']
            )

        for bond in record['bonds'].split():
            invested = Bonds(__dirname, bond).get_one(id=bond)
            investor.set_bond_ownership(
                stock_name=invested['stock_name'],
                num_shares=invested['num_shares'],
                purchased=invested['purchased'],
                investor=record['id'],
                purchase_amount=invested['purchase_amount'],
                current_price=invested['current_price'],
                coupon=invested['coupon'],
                bond_yield=invested['bond_yield']
            )
        
        assignment7_investors.append(investor)

    with open(os.path.join(__dirname, 'carterk_assignment7.md'), 'w+') as f:
        title = 'Investor Details\n'
        f.write(title)
        f.write(''.join(['=' for x in range(0, len(title))]) + '\n')

        for investor in assignment7_investors:
            investor_title = investor.get_investor_full_name()
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
            f.write('* ' + investor.get_investor_email() + '\n')
            
            f.write('### Stocks\n')
            f.write(investor.print_stock_details())

            f.write('### Bonds\n')
            f.write(investor.print_bond_details())

# Actual program processor. The carterk_assignment7.json must be in the same directory
# as the carterk_assignment7.py in order for this program to work.
dirname, filename = os.path.split(os.path.abspath(__file__))
try:
    with open(os.path.join(dirname, 'carterk_assignment7.json')) as document:
        data = json.load(document)
        assignment7_create_db(data, dirname)
        assignment7_create_output(data, dirname)
except FileNotFoundError as notfound:
    print('There is no data to process.')