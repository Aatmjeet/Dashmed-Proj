# Introduction
 Following is the API solution to question 1 of Dashmed's
 Assessment
 

## Install steps
We start with creating a virtual environment,
I am calling it ```virtual```. You can replace it with any name.

```shell
python3 -m venv virtual
```
Followed by activating the environment,

```shell
source virtual/bin/activate
```

Once we are done with install steps,
We install the dependencies
```shell
python3 install -r requirements.txt  --ignore-installed
```
And we go inside our django app to configure final few things
```shell
cd Dashmed
```
We want to add create a
```.env``` file and add the database credentials in that.
```.env``` file should be of the following format containing,
```
DB_NAME=mydatabase
DB_USER=mydatabaseuser
DB_PASSWORD=mypassword
DB_HOST=localhost
DB_PORT=5432
```
--- 

## Running the application
After setup we migrate models to database using
```shell
python3 manage.py migrate
```
Finally run server using,
```shell
python3 manage.py runserver
```