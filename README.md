Simple CRUD Example build in Django Rest framework.

Pre-requisites:

PostgresSQL DB
Python 3.8
 -----------
How to run:

In your local machine follow the next steps:

step 1:

Create an .emv file and store the enviable secrets, one example of the .env file is provided

sep 2:

In a console run the next comdands: 
`pip install -r requirements.txt`
`python manage.py makemigrations`
`python manage.py migrate`

step 3:

to run the app execute: `python manage.py runserver`

-----------------

If you want to run inside a docker, you need to have docker installed and availabe.

`Dockerfile` and `docker-compose.yaml` files are provided. Just ensure that the credential for database are setting up
in .yaml file and the settings.py

Just run `docker-compose up --build`