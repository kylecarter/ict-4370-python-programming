'''
/**
 * Assignment 8 | ICT 4370 | Python Programming
 *
 * This assignment will allow you to practice visualizing data. Continue
 * working on the project you constructed in the previous lessons.
 *
 * Import the values from the JSON file for the stocks in the portfolio.
 * The stock quotes included in the JSON file start with the purchase dates
 * of the stock, so not all start dates are the same, so you will need to
 * create different date lists to associate with the stock prices. Graph (with
 * a simple line graph) the stock prices. Show the dates on the x-axis of the
 * graph. For this graph use the closing price. Given that the value of Google
 * is so high the other lines of the graph may appear fairly flat and low.
 *
 * If you had trouble using dictionaries and classes in the past, feel free to
 * build simple lists for the JSON data to complete the assignment.
 *
 * Extra credit (3.5 points):
 *
 * Generate a portfolio total value list by date and create a histogram graph
 * for it. Since not all purchases happened on the same date, the portfolio
 * will show some jumps as new capital went into stock purchases, but you do
 * not need to worry about marking that. You have the purchase dates and the
 * quantities in the previous data.
 *
 * Since the graphic libraries accept lists, the easiest thing to do will be
 * to generate some lists from the data to create the graphs.
 *
 * Save the graphs to a file with a .png format. Instead of using the show
 * function, you would use the savefig function instead, for example:
 *
 * plt.savefig('simplePlot.png')
 *
 * Note that if you run the show first, the output created may be blank.
 *
 * @category   Assignment
 * @package    AssignmentEight
 * @author     Kyle A. Carter <kyle.carter@du.edu>
 * @copyright  2019 Kyle A. Carter
 * @license    https://opensource.org/licenses/GPL-3.0  GNU General Public License version 3
 * @version    Git: 1.0.0
 * @link       https://github.com/kylecarter/ict-4370-python-programming
 *
 */
'''

# Run using Python 3 with SQLite 3
import datetime
import json
import os
import pygal

from carterk_assignment8_stock import Stock

class AssignmentEight:

    def __init__(self, stocks, __dirname):
        """
        Creates the assignment and provides
        @param {dict} self current class instance
        @param {dict} stocks the import json
        @param {dict} __dirname excution directory of the script
        """
        self.dirname = __dirname
        self.json = stocks
        self.portfolio = self.sort_stocks()


    def sort_stocks(self):
        """
        Organizes the stocks in the JSON file based on the stock symbol name. This
        creates a dict where the keys are symbol names and the values are lists
        of stock objects.

        @param {dict} self current class instance
        @return {dict} portfolio the sorted dict of stock objects
        """
        portfolio = {}

        for obj in self.json:
            stock = Stock(
                symbol=obj['Symbol'],
                date=obj['Date'],
                open=obj['Open'],
                high=obj['High'],
                low=obj['Low'],
                close=obj['Close'],
                volume=obj['Volume']
            )

            if stock.symbol.lower() in portfolio:
                portfolio[stock.symbol.lower()].append(stock)
            else:
                portfolio[stock.symbol.lower()] = [stock]

        return portfolio

    def get_average(self, lst):
        """
        Returns the average of a list of numbers.

        @param {list} lst the list of numbers
        @return {float} the avearge of the list of numbers.
        """
        return sum(lst) / len(lst)

    def get_line_graph(self):
        """
        Creates a line graph with Pygal of the stock purchase
        date and closing price. Stocks are mapped by symbol name.
        Bases chart data on the yearly average closing costs.

        @param {dict} self current class instance
        @return {pygal} a line graph of the stock data
        """
        years = []
        closing_prices = {}
        for stocks in self.portfolio:

            for stock in self.portfolio[stocks]:
                years.append(stock.date.year)

                if not stock.symbol in closing_prices:
                    closing_prices[stock.symbol] = {}

                if not stock.date.year in closing_prices[stock.symbol]:
                    closing_prices[stock.symbol][stock.date.year] = [
                        stock.close]
                else:
                    closing_prices[stock.symbol][stock.date.year].append(
                        stock.close)
        years = list(set(years))
        years.sort()

        chart = pygal.Line()
        chart.title = 'Stock Closing Prices Yearly Averages'
        chart.x_labels = map(str, years)
        for stock, yearly_values in closing_prices.items():
            chart.add(stock, [self.get_average(yearly_values[year])
                            if year in yearly_values else None for year in years])
        chart.render_to_file(os.path.join(
            self.dirname, 'carterk_assignment8_line.svg'))


    def get_histogram_graph(self):
        """
        Creates a histogram graph with Pygal of the stock purchases by
        date and closing price. Stocks are mapped by symbol name.
        Chart data is based on the monthly average closing costs per year.

        @param {dict} self current class instance
        @return {pygal} a histogram graph of the stock data
        """
        dates = []
        closing_prices = {}
        for stocks in self.portfolio:

            for stock in self.portfolio[stocks]:
                label = stock.date.strftime('%Y-%b')
                dates.append(label)

                if not stock.symbol in closing_prices:
                    closing_prices[stock.symbol] = {}

                if not label in closing_prices[stock.symbol]:
                    closing_prices[stock.symbol][label] = []

                closing_prices[stock.symbol][label].append(stock.close)
        dates = list(set(dates))

        style = pygal.style.Style(
            label_font_size=12
        )
        hist = pygal.Histogram(x_label_rotation=20, style=style)
        hist.title = 'Stock Closing Prices Monthly Averages'

        date_format = '%Y-%b'
        labels = []
        for stock, monthly_values in closing_prices.items():
            bars = []

            for month, prices in monthly_values.items():
                date = datetime.datetime.strptime(month, date_format)
                abscissa_end = datetime.datetime(
                    date.year, date.month, 1) + datetime.timedelta(days=32)
                bars.append((
                    self.get_average(prices),
                    date.timestamp(),
                    abscissa_end.timestamp()
                ))
                labels.append(date.timestamp())
                labels.append(abscissa_end.timestamp())

            hist.add(stock, bars)
        labels = list(set(labels))
        hist.x_labels = [datetime.datetime.fromtimestamp(
            label).strftime('%Y-%b') for label in labels]

        hist.render_to_file(os.path.join(
            self.dirname, 'carterk_assignment8_histogram.svg'))


# Actual program processor. The AllStocks.json must be in the same directory
# as the carterk_assignment8.py in order for this program to work.
dirname, filename = os.path.split(os.path.abspath(__file__))
try:
    with open(os.path.join(dirname, 'AllStocks.json')) as document:
        assignment8 = AssignmentEight(json.load(document), dirname)
        assignment8.get_line_graph()
        assignment8.get_histogram_graph()
except FileNotFoundError as notfound:
    print('There is no data to process.')
