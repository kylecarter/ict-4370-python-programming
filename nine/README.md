# Simple Django API App
To use this app you need to have both Python and NodeJS installed on a computer.

## Install
1. With an active terminal session set to the root of this project run either:
   `npm install` or `yarn install`
2. It is encouraged to install both virtualenv and virtualenvwrapper when working with Django projects.
   `pip install virtualenv` and `pip install virtualenvwrapper`
3. With [virtualenvwrapper configured](https://virtualenvwrapper.readthedocs.io/en/latest/) run:
    ```bash
    mkvirtualenv --python=python3 my_virtual_env
    # with the new env active
    pip install -r requirements.txt
    ```
4. With the requirements downloaded set up the local database:
    ```bash
    backend/manage.py migrate
    backend/manage.py loaddata --format=json backend/companions/fixtures/owners.json
    backend/manage.py loaddata --format=json backend/companions/fixtures/pets.json
    backend/manage.py loaddata --format=json backend/stocks/fixtures/symbol.json
    backend/manage.py loaddata --format=json backend/stocks/fixtures/stock.json
    ```
5. You can now run `npm run dev` and an instance of the site will be running at localhost:3000
