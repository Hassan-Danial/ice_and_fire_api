# Books API 

## Overview

Books API is REST API implemented using **django rest framework** API and a local **POSTGRESQL database**.
A local Postgresql database is created by installing PostgreSQL 14 app which creates a local server. pgAdmin4 is installed to connect to this local database server and to perform actions and query on database.
Books API perform CRUD operations:
- Create a new book in the database using POST request method
- Read a book detail from database by using GET request method with book index number in database as input
- Update the book detail in database by POST request method
- Delete a specific book from the database.
## Key Topics

* How to install the repo
* Setup Project
* List of features that the code performs
* Example to run the code features

## Installling Repository

Follow following steps to install repository on your local system
1. Before install requirements, you should install Virtual Environment tools for python project, if you have installed then activite the virtual enivronment in your project, otherwise run this command to install virtual environment in your project ```pthon3 -m venv {project_name}```
2. The names of dependencies for this repository are stored in **requirements.txt** along with versions. You can install all the dependencies using one command ```pip install -r requirements.txt``` in you virtual environment.
3. To check the tools installed in your virtual environment, you can run command like ```pip list```
4. I fyou have contributed in project and installed new dependencies as you requirements then to save new dependencies in **requirements.txt** file use command ```pip freeze > requirements.txt```
5. You should not push changes to repository along with requirement.txt which hold your dependencies. If you notice the virtual Environment file name is included in **.gitignore** file so that virtual environment does not pushed on to remote repository along with other changes. Anyone who need repo can install those dependencies with one single command.

## Setup Project

1. Install [PostgreSQL 14 app](https://postgresapp.com/downloads.html) for server of local database
2. Install [pgAdmin 4](https://www.pgadmin.org/download/pgadmin-4-macos/) for the manuplation of local database 
3. Install [Postman](https://www.postman.com/downloads/) for easier request to test the API.
4. Start Postgresql server.
5. Open postgresql command line on terminal (The instruction to do that on the Postgresql website).
6. Either create table from pgadmin or from terminal.
7. Create pgadmin server by giving the hostname as localhost among other detail neccessary to setup server.
8. Open project and run online server 
```python manage.py runserver```
Remember little datils like the django server is usually live at **http://127.0.0.1:8000/** so to make any query use this address.


## List of features that the code performs

- Create a entry in local database.
- Update in local database.
- Read from the local databse.
- Delete from clocal database.
- Query the [Ice and Fire API](https://anapioficeandfire.com/Documentation#books) and show results.

## Example to run the code features

- Query the [Ice and Fire API](https://anapioficeandfire.com/Documentation#books)
Application query the Ice and Fire API with URL input of book name. If the book is present the detail of that book will be returned otherwise a success API call meesage will be shown. The API endpoint for Ice and Fire API call is:
<pre>GET http://127.0.0.1:8000/api/external-books?name="A Game of Thrones</pre>

- Create a entry in local database.
An Entry is created in local database with the data given with the request. The endpoints can be tested with Postman. Always provide the data with in request in **Body** section and provide data in **raw** in case of JSON format data. The API endpoint for local database entry is:
<pre>POST http://127.0.0.1:8000/api/v1/books</pre>
Provide data for the databse entry in same section discussed above.

- Read a entry in local database.
All the Entries in database can be requested with this endpoint:
<pre>GET http://127.0.0.1:8000/api/v1/books</pre>

- Update an entry in local database.
Any Entry can be updated in the local database using endpoint:
<pre>PATCH http://127.0.0.1:8000/api/v1/books/11</pre>
- Delete an entry in local database.
Any Entry can be deleted in the local database using endpoint:
<pre>DELETE http://127.0.0.1:8000/api/v1/books/11</pre>
