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
from carterk_assignment5_owner import Owner


assignment5 = Owner(
    first_name="Kyle",
    middle_name="Andrew",
    last_name="Carter",
    street="1020 E. 45th St.",
    street_2="Building A, Apartment 205",
    city="Austin",
    state="TX",
    postal_code="78751",
    phone_number="5129649989"
)

stocks = (
    {
        'stock_name': 'GOOGL',
        'num_shares': 125,
        'costs': {
            'purchase_amount': '$772.88',
            'current_price': '$941.53'
        },
        'purchased': '2015-08-1'
    },
    {
        'stock_name': 'MSFT',
        'num_shares': 85,
        'costs': {
            'purchase_amount': '$56.60',
            'current_price': '$73.04'
        },
        'purchased': '2015-08-1'
    },
    {
        'stock_name': 'RDS-A',
        'num_shares': 400,
        'costs': {
            'purchase_amount': '$49.58',
            'current_price': '$55.74'
        },
        'purchased': '2015-08-1'
    },
    {
        'stock_name': 'AIG',
        'num_shares': 235,
        'costs': {
            'purchase_amount': '$54.21',
            'current_price': '$65.27'
        },
        'purchased': '2015-08-1'
    },
    {
        'stock_name': 'FB',
        'num_shares': 150,
        'costs': {
            'purchase_amount': '$124.31',
            'current_price': '$172.45'
        },
        'purchased': '2015-08-1'
    },
    {
        'stock_name': 'M',
        'num_shares': 425,
        'costs': {
            'purchase_amount': '$30.30',
            'current_price': '$23.98'
        },
        'purchased': '2017-01-10'
    },
    {
        'stock_name': 'F',
        'num_shares': 85,
        'costs': {
            'purchase_amount': '$12.58',
            'current_price': '$10.95'
        },
        'purchased': '2017-02-17'
    },
    {
        'stock_name': 'IBM',
        'num_shares': 80,
        'costs': {
            'purchase_amount': '$150.37',
            'current_price': '$145.30'
        },
        'purchased': '2017-05-12'
    },
)

for stock in stocks:
    assignment5.set_stock_ownership(
        stock_name=stock['stock_name'],
        num_shares=stock['num_shares'],
        purchased=stock['purchased'],
        owner=assignment5.id,
        purchase_amount=stock['costs']['purchase_amount'],
        current_price=stock['costs']['current_price']
    )

bonds = (
    {
        'stock_name': 'GT2:GOV',
        'num_shares': 200,
        'costs': {
            'purchase_amount': '$100.02',
            'current_price': '$100.05'
        },
        'purchased': '2017-08-01',
        'coupon': 1.38,
        'bond_yield': 1.35
    },
)

for bond in bonds:
    assignment5.set_bond_ownership(
        stock_name=bond['stock_name'],
        num_shares=bond['num_shares'],
        purchased=bond['purchased'],
        owner=assignment5.id,
        purchase_amount=bond['costs']['purchase_amount'],
        current_price=bond['costs']['current_price'],
        coupon=bond['coupon'],
        bond_yield=bond['bond_yield']
    )

print('')
print('')
print('Owner: ' + assignment5.get_owner_full_name(
    assignment5.first_name,
    assignment5.middle_name,
    assignment5.last_name
))

owner_address = assignment5.get_owner_address(
    street=assignment5.street,
    street_2=assignment5.street_2,
    city=assignment5.city,
    state=assignment5.state,
    postal_code=assignment5.postal_code,
)

for x in range(0, len(owner_address)):
    print(owner_address[x])

print(assignment5.get_owner_phone_num())
assignment5.print_stock_details()
print('')
assignment5.print_bond_details()
print('')
print('')
