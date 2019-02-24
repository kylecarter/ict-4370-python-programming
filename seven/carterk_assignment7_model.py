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
import os
import re
import sqlite3

from datetime import datetime, date


class Model():
    """
    A generic class for manageing database models. Meant to be inherited
    by other model classes to manage themselves.
    """

    def __init__(self, dirname, columns):
        """
        Sets the database table name for child model.

        @param {dict} self    current class instance
        @param {string} dirname current file paths
        """
        self.db = os.path.join(dirname, 'carterk_assignment7.db')
        self.table = "carterk_assignment7_" + self.__class__.__name__.lower()

        if columns:
            connection = sqlite3.connect(self.db)

            cursor = connection.cursor()
            params = ''

            for name, config in columns.items():
                params += ' {name} {datatype} NOT NULL DEFAULT {default},'.format(
                    name=name, datatype=config['datatype'], default=config['default']) 
            sql = """CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY,{params});""".format(
                table_name=self.table, params=params[:-1])
            cursor.execute(sql)

            connection.commit()
            connection.close()
    

    def get_all(self):
        """
        Gets all the values in a given database table.

        @param {dict} self current class instance

        @return {list} data a list of the queired data
        """
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        headers = self.get_headers(cursor)
        records = cursor.execute("SELECT * FROM {table_name};".format(
            table_name=self.table)).fetchall()
        connection.close()

        data = []
        for record in records:
            datum = {}
            for x in range(0, len(record)):
                datum[headers[x]] = record[x]
            data.append(datum)
        
        return data


    def get_headers(self, cursor):
        """
        Gets the defined table headers for the current model
        database instance.

        @param {dict} self current class instance

        @return {list} headers the current class table headers
        """
        return [x[1] for x in cursor.execute(
            "PRAGMA table_info({table_name});".format(
                table_name=self.table)).fetchall()]


    def get_one(self, **kwargs):
        """
        Checks if an email address already exists in the database. If it does
        then the user will not be added.

        @param {dict} self   current class instance
        @param {string} query  proper sql query reference

        @return {dict} investor the updated investor dict
        """
        if len(kwargs.keys()) < 1:
            return None

        query = ['{key}="{value}"'.format(
            key=key, value=value) for key, value in kwargs.items()]

        sql = """SELECT * FROM {table_name} WHERE {query};""".format(
            table_name=self.table,
            query=' AND '.join(query) if len(query) > 1 else query[0]
        )

        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        headers = self.get_headers(cursor)
        records = cursor.execute(sql).fetchall()
        connection.close()

        data = []
        for record in records:
            datum = {}
            for x in range(0, len(record)):
                datum[headers[x]] = record[x]
            data.append(datum)
        
        return data[0] if len(data) > 0 else None


    def set_one(self, model):
        """
        Maps a data object to the database and inserts it in the proper
        table.

        @param {dict} self  current class instance
        @param {dict} model data object to insert into the database

        @return {dict} investor the updated investor dict
        """
        connection = sqlite3.connect(self.db)

        cursor = connection.cursor()
        columns = 'id, '
        values = 'NULL, '
        for column in self.get_headers(cursor):
            if column == 'stocks' or column == 'bonds':
                continue
            elif column in model.keys():
                columns += '"{col}", '.format(col=column)
                values += '"{value}", '.format(value=model[column])

        sql = """INSERT INTO {table_name} ({cols}) VALUES ({values});""".format(
            table_name=self.table, cols=columns[:-2], values=values[:-2])

        cursor.execute(sql)
        record = cursor.lastrowid
        connection.commit()
        connection.close()

        return self.get_one(id=record)
    

    def update_one(self, id, **kwargs):
        """
        Maps a data object to the database and inserts it in the proper
        table.

        @param {dict} self  current class instance
        @param {dict} kwargs data to update

        @return {dict} investor the updated investor dict
        """
        if len(kwargs.keys()) < 1:
            return None

        columns = ['SET {key}="{value}"'.format(
            key=key, value=value) for key, value in kwargs.items()]

        sql = """UPDATE {table_name} {columns} WHERE {query};""".format(
            table_name=self.table,
            columns=' '.join(columns),
            query='id={id}'.format(id=id)
        )

        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        connection.close()

        return self.get_one(id=id)


class Investors(Model):
    """
    A database model for the Investor object.
    """

    def __init__(self, dirname, *args):
        """
        Creates a database object relation management connection between the
        database and the investors data model.

        @param {dict} self current class instance
        @param {list} args a list of possible arguments for the db table columns
        """
        columns = {}

        if len(args) > 0:
            columns = {
                'stocks': {
                    'datatype': 'TEXT',
                    'default': "''"
                },
                'bonds': {
                    'datatype': 'TEXT',
                    'default': "''"
                }
            }
            for arg in args:
                columns[arg] = {
                    'datatype': 'VARCHAR(255)',
                    'default': "''"
                }
        super().__init__(dirname, columns)
    

    def update_stocks(self, record, stock):
        """
        Updates the stocks values of an investor.

        @param {dict} self current class instance
        @param {int} record investor id
        @param {int} stock stock id to add

        @return {dict} investor the updated investor dict
        """
        if not record and not stock:
            return None

        investor = self.get_one(id=record)

        if investor and not str(stock) in investor['stocks'].split():
            stocks = '{current} {added}'.format(current=investor['stocks'],
                added=stock)
            return self.update_one(investor['id'], stocks=stocks)
        else:
            return self.get_one(id=record)


    def update_bonds(self, record, bond):
        """
        Updates the stocks values of an investor.

        @param {dict} self current class instance
        @param {int} record investor id
        @param {int} bond bond id to add

        @return {dict} investor the updated investor dict
        """
        if not record and not bond:
            return None

        investor = self.get_one(id=record)


        if investor and not str(bond) in investor['bonds'].split():
            bonds = '{current} {added}'.format(current=investor['bonds'],
                added=bond)
            return self.update_one(investor['id'], bonds=bonds)
        else:
            return self.get_one(id=record)


class Stocks(Model):
    """
    A database model for the Stock object.
    """

    def __init__(self, dirname, investor, *args):
        """
        Creates a database object relation management connection between the
        database and the stocks data model.

        @param {dict} self current class instance
        @param {list} args a list of possible arguments for the db table columns
        """
        columns = {}

        if len(args) > 0:
            columns = {
                'investor': {
                    'datatype': 'INTEGER',
                    'default': investor
                }
            }
            for arg in args:
                if arg == 'num_shares':
                    columns[arg] = {
                        'datatype': 'INTEGER',
                        'default': 0
                    }
                else:
                    columns[arg] = {
                        'datatype': 'VARCHAR(255)',
                        'default': "''"
                }
        super().__init__(dirname, columns)
    

    def set_one_stock(self, model):
        """
        Curates a single stock table row.

        @param {dict} self current class instance
        @param {dict} model stock instance to store

        @return {dict} investor the updated investor dict
        """
        data = {}
        for key, value in model.items():
            if key == 'costs':
                data['purchase_amount'] = model[key]['purchase_amount']
                data['current_price'] = model[key]['current_price']
            else:
                data[key] = value

        return self.set_one(data)


class Bonds(Model):
    """
    A database model for the Bond object.
    """

    def __init__(self, dirname, investor, *args):
        """
        Creates a database object relation management connection between the
        database and the bonds data model.

        @param {dict} self current class instance
        @param {list} args a list of possible arguments for the db table columns
        """
        columns = {}

        if len(args) > 0:
            columns = {
                'investor': {
                    'datatype': 'INTEGER',
                    'default': investor
                }
            }
            for arg in args:
                if arg == 'num_shares':
                    columns[arg] = {
                        'datatype': 'INTEGER',
                        'default': 0
                    }
                elif arg == 'coupon' or arg == 'bond_yield':
                    columns[arg] = {
                        'datatype': 'FLOAT',
                        'default': 0
                    }
                else:
                    columns[arg] = {
                        'datatype': 'VARCHAR(255)',
                        'default': "''"
                    }
        super().__init__(dirname, columns)


    def set_one_bond(self, model):
        """
        Curates a single bond table row.

        @param {dict} self current class instance
        @param {dict} model bond instance to store

        @return {dict} investor the updated investor dict
        """
        data = {}
        for key, value in model.items():
            if key == 'costs':
                data['purchase_amount'] = model[key]['purchase_amount']
                data['current_price'] = model[key]['current_price']
            else:
                data[key] = value

        return self.set_one(data)

